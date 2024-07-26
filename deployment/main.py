from fastapi import FastAPI, File, UploadFile
import functions as fc
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import db
from fastapi.responses import JSONResponse
import ragChat
import verifyResults
import re

app = FastAPI()

@app.get('/')
async def homepage():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="SwasthAI API - Swagger UI",
    )

@app.post('/chat/')
async def chat(serviceName:str, secretCode: str, message: str):
    try:
        chatbot = ragChat.ragChat(kwargs={"serviceName": serviceName, "secretCode": secretCode})
        response= chatbot.get_response(message)
        return JSONResponse(content={"message": response}, status_code=200)
    except Exception as e:
        return JSONResponse(content= {"error": str(e)}, status_code=401)
    
@app.post("/verifyResults")
async def verifyResultsa(
    diseaseName: str = None,
    serviceName: str = None,
    secretCode: str = None,
    file: UploadFile = File(...),
):
    try:
        verifier= verifyResults.verifyScanResult(diseaseName=diseaseName, serviceName=serviceName, secretCode=secretCode)

        file_location = f"temp_files/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        
        with open(file_location, "wb") as f:
            f.write(await file.read())
         
        match serviceName:
            case "google":
                 result= verifier.verifyResultsGoogle(file_location)
            case "openai":
                result=  verifier.verifyResultsOpenAI(file_location)
            case _:
                result=  JSONResponse(content= {"error": "Invalid service name"}, status_code=401)

        print(result)
        os.remove(file_location)
        return JSONResponse(content=result, status_code=200)
 
    except Exception as e:
        return JSONResponse(content= {"error": str(e)}, status_code=401)

@app.get('/getUsername/{name}')
async def get_username(name: str):
    load_dotenv()
    cred= json.loads(os.environ["FIREBASE_CREDENTIALS"])
    cred1= firebase_admin.credentials.Certificate(cred)
    if not firebase_admin._apps:
        app=firebase_admin.initialize_app(cred1, {"databaseURL":"https://medbuddy-ai-default-rtdb.asia-southeast1.firebasedatabase.app/"})
    ref= db.reference("users")
    list= ref.get()
    for user in list:
        if name==list[user]['username']:
            return list[user]
    return {
        "firstName": None,
        "lastName": None,
        "username": None
}

@app.get('/gen')
async def data():
    return fc.getDoctorGeneralMedApollo()

@app.get('/symptoms/{symptom_sentence}')
async def symptoms(symptom_sentence: str):
    return fc.getAISymptomsResponse(symptom_sentence)

@app.get('/next_symptom/{symptom_sentence}')
async def next_symptom(symptom_sentence: str):
    return fc.getSymptomPredictionResponse(symptom_sentence)

@app.post('/upload')
async def decodeReport(file: UploadFile = File(...)):
    try:
        # Read the file into memory
        contents = await file.read()
        #image = Image.open(BytesIO(contents))

        # Perform analysis on the image
        #analysis_result = analyze_image(image)

        return JSONResponse(
            content={
                "message": "Image processed successfully", 
                "analysis": "analysis_result"
            }, 
            status_code=200
        )
    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred: {str(e)}"}, status_code=500)
    

    def parse_error_message(error_str):
        try:
            # Try to parse the error string as JSON
            error_dict = json.loads(error_str)
            if isinstance(error_dict, dict) and 'error' in error_dict:
                return error_dict['error']['message']
        except json.JSONDecodeError:
            pass

        # If JSON parsing fails, use regex to extract the message
        match = re.search(r"'message': '(.+?)'", error_str)
        if match:
            return match.group(1)

        # If all else fails, return the original error string
        return error_str
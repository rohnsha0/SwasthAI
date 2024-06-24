from fastapi import FastAPI, File, UploadFile
import functions as fc
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import Info
import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import db
from fastapi.responses import JSONResponse
from io import BytesIO
#from PIL import Image

app = FastAPI()

@app.get('/')
async def homepage():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="SwasthAI API - Swagger UI",
    )

@app.get('/chat/{message}')
async def chat(message: str):
    return fc.getChatResponse(message)


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

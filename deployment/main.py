from fastapi import FastAPI
import functions as fc
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import Info
import os
from dotenv import load_dotenv
import json
import firebase_admin
from firebase_admin import db

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
    return "userNotFound"

@app.get('/gen')
async def data():
    return fc.getDoctorGeneralMedApollo()

@app.get('/symptoms/{symptom_sentence}')
async def symptoms(symptom_sentence: str):
    return fc.getAISymptomsResponse(symptom_sentence)

@app.get('/next_symptom/{symptom_sentence}')
async def next_symptom(symptom_sentence: str):
    return fc.getSymptomPredictionResponse(symptom_sentence)

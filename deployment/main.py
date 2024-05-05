from fastapi import FastAPI
import functions as fc
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import Info

app = FastAPI()
#handler = Mangum(app)

@app.get('/')
async def homepage():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="SwasthAI API - Swagger UI",
    )

@app.get('/chat/{message}')
async def chat(message: str):
    return fc.getChatResponse(message)


@app.get('/gen')
async def data():
    return fc.getDoctorGeneralMedApollo()

@app.get('/symptoms/{symptom_sentence}')
async def symptoms(symptom_sentence: str):
    return fc.getAISymptomsResponse(symptom_sentence)

@app.get('/next_symptom/{symptom_sentence}')
async def next_symptom(symptom_sentence: str):
    return fc.getSymptomPredictionResponse(symptom_sentence)

from fastapi import FastAPI
import functions as fc

app = FastAPI()
#handler = Mangum(app)

@app.get('/')
async def homepage():
    return {
        'welcome': "title"
    }

@app.get('/chat/{message}')
async def chat(message: str):
    return fc.getChatResponse(message)


@app.get('/gen')
async def data():
    return fc.getDoctorGeneralMedApollo()

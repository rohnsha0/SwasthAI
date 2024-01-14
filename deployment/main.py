from fastapi import FastAPI
from mangum import Mangum
import functions as fc

app = FastAPI()
handler = Mangum(app)

@app.get('/')
async def homepage():
    return {
        'welcome': "title"
    }


@app.get('/gen')
async def data():
    return fc.getDoctorGeneralMedApollo()

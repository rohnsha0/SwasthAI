from fastapi import FastAPI, File, UploadFile
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import Info
from fastapi.responses import JSONResponse
from llama_cpp import Llama
import os

app = FastAPI()

@app.get('/')
async def homepage():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="SwasthAI API - Swagger UI",
    )

@app.get('/llma')
async def llma():
    try: 
        model_path= os.path.join("tinyllama-1.1b-chat-v1.0.Q8_0.gguf")
        llm = Llama(model_path=model_path)
        return {"message": "Hello World"}
    except Exception as e:
        return {"message": str(e)}
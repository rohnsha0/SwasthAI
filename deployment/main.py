from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import cv2

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("lungsV1")

CLASS_NAMES = ['normal', 'pneumonia', 'tuberculosis']


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    image = cv2.resize(image, (256, 256))
    return image

@app.get('/')
async def wel():
    return {
        'welcome': 'access'
    }

@app.post('/upload/')
async def uplaod(
        file: UploadFile = File(...)
):
    try:
        return {
            'file': file.filename
        }
    except:
        return {
            'errorer': "inv"
        }


@app.post("/predict/")
async def predict(
        file: UploadFile = File(...)
):
    #image = read_file_as_image(await file.read())
    #img_batch = np.expand_dims(image, 0)

    image = read_file_as_image(await file.read())
    image = image / 255.0  # Normalize the pixel values to [0, 1]
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = tf.image.resize(image, [256, 256], method=tf.image.ResizeMethod.BILINEAR)
    image = tf.expand_dims(image, axis=0)

    predictions = MODEL.predict(image)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
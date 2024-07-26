import os
import google.generativeai as genai
import json
from openai import OpenAI
import base64
import requests

class verifyScanResult:
    def __init__(self,
            diseaseName: str = None,
            serviceName: str = None,
            secretCode: str = None):
        self.diseaseName = diseaseName
        self.serviceName = serviceName
        self.secretCode = secretCode
        self.prompt = f"""
Task: Determine if the image shows evidence of {self.diseaseName}.
    
    Instructions:
    1. Examine the image for any signs or indicators of {self.diseaseName}.
    2. Consider the typical presentation of {self.diseaseName} in this type of medical image.
    3. Assess the confidence level of your determination.
    4. Provide your analysis in a structured JSON format.
    
    Return your analysis as a JSON object with the following structure:
    {{
        "isMatched": boolean,  // true if the disease is detected, false otherwise
        "confidence": float,  // a value between 0 and 1, where 1 is highest confidence
    }}
    
    Important: Ensure your response can be parsed as valid JSON. Do not include any text outside the JSON structure.
"""
    
    def verifyResultsGoogle(self, filePath, mime_type=None):

        genai.configure(api_key=self.secretCode)

        def upload_to_gemini():
            file = genai.upload_file(filePath, mime_type=mime_type)
            print(f"Uploaded file '{file.display_name}' as: {file.uri}")
            return file

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 1000,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
        )

        chat_session = model.start_chat(
        history=[
        ]
        )

        response = chat_session.send_message(
            [upload_to_gemini(),
            self.prompt]
            )

        print(response.text)
        return json.loads(response.text)
    
    def verifyResultsOpenAI(self, filePath, mime_type=None):

        client= OpenAI(api_key=self.secretCode)
    
        def encode_image():
            with open(filePath, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
            
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.secretCode}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": self.prompt
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{encode_image()}"
                    }
                    }
                ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        return json.loads(response.text)
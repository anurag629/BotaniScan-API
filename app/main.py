from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from uvicorn import run
import os
from PIL import Image
import requests


import app.internal.plantClass as aip
import app.models.getModel as apg
import app.chatbot.chatBot as acc
import app.chatbot.generalChatBot as acgc

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)


# Get method for getting the prediction of the image
@app.get("/")
async def root():
    return {"message": "Welcome to the BOTANISCAN API!"}


# Get method for getting the prediction of the image
@app.post("/prediction/")
async def get_image_prediction(image_link: str = ""):
    if image_link == "":
        return {"message": "No image link provided"}
    
    try:
        image = Image.open(requests.get(image_link, stream=True).raw)
    except:
        return {"message": "Invalid image link"}

    pred = apg.getPrediction(image)

    max_score = -1
    max_score_label = ""

    for item in pred:
        if item["score"] > max_score:
            max_score = item["score"]
            max_score_label = item["label"]

    detail = acc.get_plant_details(max_score_label)
    
    return {"prediction": pred, "detail": detail}


# Get the plant details
@app.get("/plant_details/{plant_name}")
async def get_plant_details(plant_name: str):
    return {"detail": acc.get_plant_details(plant_name)}


# Get method for getting all the classes in the model
@app.get("/classes")
async def get_all_classes():
    return {"classes": aip.getAllClasses()}


# Get method for chatting with biodiversity researcher
@app.post("/chat/biodiversity_researcher")
async def chat_with_expert_biodiversity_researcher(message: str = "", examples: list = []):
    if message == "":
        return {"response": "No message provided"}
    
    return {"response": acgc.chat_with_expert_biodiversity_researcher(message, examples)}

    
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	run(app, host="0.0.0.0", port=port)
      
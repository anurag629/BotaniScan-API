from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import tensorflow as tf
from tensorflow.keras.utils import get_file 
from tensorflow.keras.utils import load_img 
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from numpy import max
import numpy as np
from json import dumps
import cv2
from uvicorn import run
import os
from PIL import Image
import requests


import app.internal.plantClass as aip
import app.models.getModel as apg


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

@app.get("/")
async def root():
    return {"message": "Welcome to the Food Vision API!"}


@app.post("/prediction/")
async def get_image_prediction(image_link: str = ""):
    if image_link == "":
        return {"message": "No image link provided"}
    
    image = Image.open(requests.get(image_link, stream=True).raw)

    pred = apg.getPrediction(image)

    return {"prediction": pred}


# Get method for getting all the classes in the model
@app.get("/classes")
async def get_all_classes():
    return {"classes": aip.getAllClasses()}


@app.get("/tf_version")
async def predict():
    return {"message": f"Hello, {tf.__version__}"}

    
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	run(app, host="0.0.0.0", port=port)
      
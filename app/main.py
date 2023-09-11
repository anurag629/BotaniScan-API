from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import tensorflow as tf
from tensorflow.keras.models import load_model
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


import app.internal.plantClass as aip


app = FastAPI()

# model_dir = "../models/model_01.h5"
# model = load_model(model_dir, compile=False)

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


# @app.post("/prediction/")
# async def get_net_image_prediction(image_link: str = ""):
#     if image_link == "":
#         return {"message": "No image link provided"}
    
#     img_path = get_file(
#         origin = image_link
#     )
#     img = load_img(
#         img_path, 
#         target_size = (250, 250)
#     )

#     img_array = img_to_array(img)
#     img_array = expand_dims(img_array, 0)

#     pred = model.predict(img_array)
#     score = softmax(pred[0])
#     print(score)

#     class_prediction = aip.getClassName(score)
#     model_score = round(max(score) * 100, 2)

#     return {
#         "model-prediction": class_prediction,
#         "model-prediction-confidence-score": model_score
#     }


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
      
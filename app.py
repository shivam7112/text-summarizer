from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textsummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization"

app = FastAPI()

@app.get("/", tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training sucessfull!")
    except Exception as e:
        return Response(f"Error Occured {e}")


@app.post("/prediction")
async def prediction_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        return Response(f"Error Occured {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
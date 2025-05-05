# api/index.py
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os, base64

app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "ok"}

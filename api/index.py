from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    flag = os.getenv("FLAG", "FLAG NOT FOUND")
    return HTMLResponse(content=f"<h1>Hello from FastAPI!</h1><p>Flag: {flag}</p>")

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import base64
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory="templates")

USERS = {
    "admin": "supersecurepassword"
}

@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    flag = os.getenv("FLAG", "CTF{dummy_flag}")
    if USERS.get(username) == password:
        encoded_flag = base64.b64encode(flag.encode()).decode()
        response = templates.TemplateResponse("success.html", {"request": request, "flag": encoded_flag})
        response.set_cookie("SESSIONID", encoded_flag)
        return response
    return HTMLResponse("<h1>ACCESS DENIED</h1>")

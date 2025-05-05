from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    flag = os.getenv("FLAG", "FLAG NOT FOUND")
    return HTMLResponse(content=f"<h1>Hello from FastAPI!</h1><p>Flag: {flag}</p>")

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password123":
        flag = os.getenv("FLAG", "FLAG NOT FOUND")
        response = HTMLResponse(content="ACCESS GRANTED<br><img src='/flag.png'/>")
        response.set_cookie(key="SESSIONID", value=base64.b64encode(flag.encode()).decode())
        return response
    return HTMLResponse(content="ACCESS DENIED", status_code=403)

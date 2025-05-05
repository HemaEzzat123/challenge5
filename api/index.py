# api/index.py
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os, base64

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
        <form action="/api/login" method="post">
            <input name="username" placeholder="username" required>
            <input name="password" type="password" placeholder="password" required>
            <input type="submit" value="Login">
        </form>
    """

@app.post("/login", response_class=HTMLResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        flag = os.getenv("FLAG", "FLAG NOT FOUND")
        session = base64.b64encode(flag.encode()).decode()
        res = HTMLResponse(content="ACCESS GRANTED<br><img src='/flag.png'>")
        res.set_cookie("SESSIONID", session)
        return res
    return HTMLResponse("ACCESS DENIED", status_code=403)

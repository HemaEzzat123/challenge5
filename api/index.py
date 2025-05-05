from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os, base64, traceback

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def login_page():
    return HTMLResponse("""
        <form action="/login" method="post">
            <input type="text" name="username" required>
            <input type="password" name="password" required>
            <input type="submit" value="submit">
        </form>
    """)

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    try:
        if username == "admin" and password == "password123":
            flag = os.getenv("FLAG", "FLAG NOT FOUND")
            res = HTMLResponse(content="ACCESS GRANTED<br><img src='/flag.png'/>")
            res.set_cookie(key="SESSIONID", value=base64.b64encode(flag.encode()).decode())
            return res
        return HTMLResponse(content="ACCESS DENIED", status_code=403)
    except Exception:
        return HTMLResponse(content=f"<pre>{traceback.format_exc()}</pre>", status_code=500)

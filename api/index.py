from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import base64
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Simulate a "database"
USERS = {
    "admin": "supersecurepassword",
    "guest": "guest123"
}

@app.get("/api/")
def login_page():
    return HTMLResponse("""
    <html>
    <head><title>Vault</title></head>
    <body>
        <h1>Vault</h1>
        <form method="POST" action="/api/">
            <input name="username" type="text" placeholder="username" required />
            <input name="password" type="password" placeholder="password" required />
            <input type="submit" value="submit" />
        </form>
    </body>
    </html>
    """)

@app.post("/api/")
async def login(username: str = Form(...), password: str = Form(...)):
    flag = os.getenv("FLAG", "CTF{no_flag}")
    if username in USERS and USERS[username] == password:
        encoded_flag = base64.b64encode(flag.encode()).decode()
        html = f"""
        <html>
        <body>
            <h1>ACCESS GRANTED</h1>
            <img src="/flag.png" alt="flag" />
        </body>
        </html>
        """
        response = HTMLResponse(content=html)
        response.set_cookie(key="SESSIONID", value=encoded_flag)
        return response
    else:
        return HTMLResponse("<h1>ACCESS DENIED</h1>")

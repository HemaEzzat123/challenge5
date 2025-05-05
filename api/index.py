from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import base64
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

USERS = {
    "admin": "supersecurepassword"
}

@app.get("/")
def show_form():
    return HTMLResponse("""
        <html>
        <body>
            <h1>Vault</h1>
            <form method="POST">
                <input name="username" type="text" placeholder="username" required />
                <input name="password" type="password" placeholder="password" required />
                <input type="submit" value="submit" />
            </form>
        </body>
        </html>
    """)

@app.post("/")
async def login(username: str = Form(...), password: str = Form(...)):
    flag = os.getenv("FLAG", "CTF{dummy_flag}")
    if USERS.get(username) == password:
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
        response.set_cookie("SESSIONID", encoded_flag)
        return response
    return HTMLResponse("<h1>ACCESS DENIED</h1>")

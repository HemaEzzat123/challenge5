from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import mysql.connector
import os
import base64

app = FastAPI()

# Serve CSS and image files
app.mount("/css", StaticFiles(directory="static/css"), name="css")
app.mount("/flag.png", StaticFiles(directory="static"), name="flag")

@app.get("/", response_class=HTMLResponse)
async def login_form():
    html = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Vault</title>
        <link rel="stylesheet" type="text/css" href="/css/main.css">
    </head>
    <body>
        <div class="main">
            <h1 class="heading">Vault</h1>
            <div class="form">
                <form action="/login" method="post">
                    <input type="text" name="username" placeholder="username" required>
                    <input type="password" name="password" placeholder="password" required>
                    <input type="submit" value="submit">
                </form>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    try:
        conn = mysql.connector.connect(
            host="database",
            user="root",
            password="password",
            database="vault"
        )
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            # Get flag from environment (best for Vercel)
            flag = os.getenv("FLAG", "FLAG NOT FOUND")
            encoded_flag = base64.b64encode(flag.encode()).decode()
            response = HTMLResponse(content=f"""
                <html>
                <head>
                    <title>Login</title>
                    <link rel="stylesheet" type="text/css" href="/css/main.css">
                </head>
                <body>
                    <div class="main">
                        <h1 class="heading">ACCESS GRANTED<br>
                        <img src="/flag.png" alt="flag"/>
                        </h1>
                    </div>
                </body>
                </html>
            """)
            response.set_cookie(key="SESSIONID", value=encoded_flag)
            return response
        else:
            return HTMLResponse(content="""
                <html><body><h1 class="heading">ACCESS DENIED</h1></body></html>
            """)
    except Exception as e:
        return HTMLResponse(content=f"Challenge is dead: {str(e)}")

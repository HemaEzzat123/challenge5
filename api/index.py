from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import base64
import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create app
app = FastAPI()

# Create static directories if they don't exist
os.makedirs("static/images", exist_ok=True)
os.makedirs("static/css", exist_ok=True)

# Create a placeholder flag image if it doesn't exist
if not os.path.exists("static/images/flag.png"):
    # Create a simple text file to notify about missing image
    with open("static/images/flag.png", "wb") as f:
        # This is a tiny transparent PNG - replace with real flag.png
        tiny_png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
        f.write(tiny_png)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define users
USERS = {
    "admin": "supersecurepassword"
}

@app.get("/")
def show_form():
    return HTMLResponse("""
        <html>
        <head>
            <title>Halib Al-Khair</title>
            <style>
            /* Global Styles */
            :root {
                --primary-color   : #1a5f7a;
                --secondary-color : #88c0d0;
                --accent-color    : #2e3440;
                --text-color      : #2e3440;
                --background-color: #eceff4;
            }

            * {
                margin    : 0;
                padding   : 0;
                box-sizing: border-box;
            }

            body {
                font-family     : 'Arial', sans-serif;
                line-height     : 1.6;
                color           : var(--text-color);
                background-color: var(--background-color);
            }

            a {
                text-decoration: none;
                color          : inherit;
            }

            /* Header & Navigation */
            header {
                background-color: white;
                box-shadow      : 0 2px 5px rgba(0, 0, 0, 0.1);
                position        : sticky;
                top             : 0;
                z-index         : 10;
            }

            nav {
                max-width      : 1200px;
                margin         : 0 auto;
                padding        : 1rem;
                display        : flex;
                justify-content: space-between;
                align-items    : center;
            }

            .logo img {
                height: 50px;
            }

            nav ul {
                display   : flex;
                list-style: none;
            }

            nav ul li {
                margin-left: 2rem;
            }

            nav ul li a {
                color      : var(--text-color);
                font-weight: 500;
                transition : color 0.3s ease;
            }

            nav ul li a:hover {
                color: var(--primary-color);
            }

            /* Hero Section */
            .hero {
                text-align: center;
                padding   : 4rem 1rem;
                background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9));
                border-radius: 10px;
                margin       : 2rem auto;
                max-width    : 1200px;
            }

            .hero h1 {
                font-size    : 3rem;
                color        : var(--primary-color);
                margin-bottom: 1rem;
            }

            .hero p {
                font-size: 1.2rem;
            }

            /* Login Form */
            .login {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }

            .login h2 {
                text-align: center;
                margin-bottom: 20px;
                color: var(--primary-color);
            }

            .login input {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

            .login input[type="submit"] {
                background-color: var(--primary-color);
                color: white;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

            .login input[type="submit"]:hover {
                background-color: var(--secondary-color);
            }

            /* Flag Image */
            .flag-container {
                text-align: center;
                margin: 30px 0;
            }

            .flag-container h1 {
                color: var(--primary-color);
                margin-bottom: 20px;
            }

            .flag-container img {
                max-width: 100%;
                height: auto;
                border: 2px solid var(--accent-color);
                border-radius: 5px;
            }

            /* Product Section */
            .featured-products {
                max-width: 1200px;
                margin   : 0 auto;
                padding  : 2rem 1rem;
            }

            .featured-products h2 {
                text-align   : center;
                font-size    : 2rem;
                margin-bottom: 2rem;
                color        : var(--primary-color);
            }

            .product-grid {
                display              : grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap                  : 2rem;
            }

            .product-card {
                background   : white;
                border-radius: 10px;
                padding      : 1rem;
                text-align   : center;
                box-shadow   : 0 2px 5px rgba(0, 0, 0, 0.1);
                transition   : transform 0.3s ease;
            }

            .product-card:hover {
                transform: translateY(-5px);
            }

            .product-card h3 {
                margin-bottom: 0.5rem;
                color        : var(--accent-color);
            }

            .product-card p {
                font-size    : 0.95rem;
                margin-bottom: 1rem;
            }

            .btn {
                display         : inline-block;
                padding         : 0.5rem 1rem;
                background-color: var(--primary-color);
                color           : white;
                border-radius   : 5px;
                transition      : background-color 0.3s ease;
            }

            .btn:hover {
                background-color: var(--secondary-color);
            }

            /* Footer */
            footer {
                text-align      : center;
                padding         : 2rem;
                background-color: var(--accent-color);
                color           : white;
                margin-top      : 3rem;
            }
            </style>
        </head>
        <body>
            <header>
                <nav>
                    <div class="logo"></div>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/products">Products</a></li>
                        <li><a href="/reports/generate">Reports</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </nav>
            </header>

            <main>
                <section class="hero">
                    <h1>Welcome to Halib Al-Khair</h1>
                    <p>Delivering the finest dairy products since 1985</p>
                </section>

                <section class="login">
                    <h2>Vault Login</h2>
                    <form method="POST">
                        <input name="username" type="text" placeholder="username" required />
                        <input name="password" type="password" placeholder="password" required />
                        <input type="submit" value="Submit" />
                    </form>
                </section>

                <section class="featured-products">
                    <h2>Our Premium Products</h2>
                    <div class="product-grid">
                        <div class="product-card">
                            <h3>Fresh Milk</h3>
                            <p>Farm-fresh whole milk</p>
                            <a href="/products?id=1" class="btn">Learn More</a>
                        </div>
                        <div class="product-card">
                            <h3>Natural Yogurt</h3>
                            <p>Creamy and healthy</p>
                            <a href="/products?id=2" class="btn">Learn More</a>
                        </div>
                    </div>
                </section>
            </main>

            <footer>
                <p>&copy; 2024 Halib Al-Khair. All rights reserved.</p>
            </footer>
        </body>
        </html>
    """)

# Direct route to serve the flag image for testing
@app.get("/flag-image")
async def serve_flag_image():
    return FileResponse("static/images/flag.png")

@app.post("/")
async def login(username: str = Form(...), password: str = Form(...)):
    flag = os.getenv("FLAG", "CTF{dummy_flag}")
    if USERS.get(username) == password:
        encoded_flag = base64.b64encode(flag.encode()).decode()
        html = """
        <html>
        <head>
            <title>Halib Al-Khair - Access Granted</title>
            <style>
            /* Global Styles */
            :root {
                --primary-color   : #1a5f7a;
                --secondary-color : #88c0d0;
                --accent-color    : #2e3440;
                --text-color      : #2e3440;
                --background-color: #eceff4;
            }

            * {
                margin    : 0;
                padding   : 0;
                box-sizing: border-box;
            }

            body {
                font-family     : 'Arial', sans-serif;
                line-height     : 1.6;
                color           : var(--text-color);
                background-color: var(--background-color);
            }

            a {
                text-decoration: none;
                color          : inherit;
            }

            /* Header & Navigation */
            header {
                background-color: white;
                box-shadow      : 0 2px 5px rgba(0, 0, 0, 0.1);
                position        : sticky;
                top             : 0;
                z-index         : 10;
            }

            nav {
                max-width      : 1200px;
                margin         : 0 auto;
                padding        : 1rem;
                display        : flex;
                justify-content: space-between;
                align-items    : center;
            }

            .logo img {
                height: 50px;
            }

            nav ul {
                display   : flex;
                list-style: none;
            }

            nav ul li {
                margin-left: 2rem;
            }

            nav ul li a {
                color      : var(--text-color);
                font-weight: 500;
                transition : color 0.3s ease;
            }

            nav ul li a:hover {
                color: var(--primary-color);
            }

            /* Hero Section */
            .hero {
                text-align: center;
                padding   : 4rem 1rem;
                background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9));
                border-radius: 10px;
                margin       : 2rem auto;
                max-width    : 1200px;
            }

            .hero h1 {
                font-size    : 3rem;
                color        : var(--primary-color);
                margin-bottom: 1rem;
            }

            .hero p {
                font-size: 1.2rem;
            }

            /* Flag Container */
            .flag-container {
                text-align: center;
                margin: 30px auto;
                max-width: 600px;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }

            .flag-container h1 {
                color: #2ca05a;
                margin-bottom: 20px;
            }

            .flag-container img {
                max-width: 100%;
                height: auto;
                border: 2px solid var(--accent-color);
                border-radius: 5px;
            }

            /* Product Section */
            .featured-products {
                max-width: 1200px;
                margin   : 0 auto;
                padding  : 2rem 1rem;
            }

            .featured-products h2 {
                text-align   : center;
                font-size    : 2rem;
                margin-bottom: 2rem;
                color        : var(--primary-color);
            }

            .product-grid {
                display              : grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap                  : 2rem;
            }

            .product-card {
                background   : white;
                border-radius: 10px;
                padding      : 1rem;
                text-align   : center;
                box-shadow   : 0 2px 5px rgba(0, 0, 0, 0.1);
                transition   : transform 0.3s ease;
            }

            .product-card:hover {
                transform: translateY(-5px);
            }

            .product-card h3 {
                margin-bottom: 0.5rem;
                color        : var(--accent-color);
            }

            .product-card p {
                font-size    : 0.95rem;
                margin-bottom: 1rem;
            }

            .btn {
                display         : inline-block;
                padding         : 0.5rem 1rem;
                background-color: var(--primary-color);
                color           : white;
                border-radius   : 5px;
                transition      : background-color 0.3s ease;
            }

            .btn:hover {
                background-color: var(--secondary-color);
            }

            /* Footer */
            footer {
                text-align      : center;
                padding         : 2rem;
                background-color: var(--accent-color);
                color           : white;
                margin-top      : 3rem;
            }
            </style>
        </head>
        <body>
            <header>
                <nav>
                    <div class="logo"></div>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/products">Products</a></li>
                        <li><a href="/reports/generate">Reports</a></li>
                        <li><a href="/about">About</a></li>
                        <li><a href="/contact">Contact</a></li>
                    </ul>
                </nav>
            </header>

            <main>
                <section class="hero">
                    <h1>Welcome to Halib Al-Khair</h1>
                    <p>Delivering the finest dairy products since 1985</p>
                </section>

                <div class="flag-container">
                    <h1>ACCESS GRANTED</h1>
                    <img src="/static/images/flag.png" alt="flag">
                    <p style="margin-top: 15px;">If the image is not visible, you can also check the SESSIONID cookie or visit <a href="/flag-image" target="_blank">/flag-image</a> directly.</p>
                </div>

                <section class="featured-products">
                    <h2>Our Premium Products</h2>
                    <div class="product-grid">
                        <div class="product-card">
                            <h3>Fresh Milk</h3>
                            <p>Farm-fresh whole milk</p>
                            <a href="/products?id=1" class="btn">Learn More</a>
                        </div>
                        <div class="product-card">
                            <h3>Natural Yogurt</h3>
                            <p>Creamy and healthy</p>
                            <a href="/products?id=2" class="btn">Learn More</a>
                        </div>
                    </div>
                </section>
            </main>

            <footer>
                <p>&copy; 2024 Halib Al-Khair. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """
        response = HTMLResponse(content=html)
        response.set_cookie("SESSIONID", encoded_flag)
        return response
    return HTMLResponse("<h1>ACCESS DENIED</h1>")
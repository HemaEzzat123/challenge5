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
        <head>
            <title>Halib Al-Khair</title>
            <link rel="stylesheet" href="../static/css/main.css">
        </head>
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
    background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)),
        url('/static/images/hero-bg.jpg') center/cover no-repeat;
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

.product-card img {
    width        : 100%;
    height       : 200px;
    object-fit   : cover;
    border-radius: 5px;
    margin-bottom: 1rem;
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

/* Meme Image for Debug or Branding */
img[alt="meme image"] {}
        </style>
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

                <section style="margin-left: 500px;" class="login">
                    <h2>Vault Login</h2>
                    <form method="POST">
                        <input name="username" type="text" placeholder="username" required />
                        <input name="password" type="password" placeholder="password" required />
                        <input type="submit" value="submit" />
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

@app.post("/")
async def login(username: str = Form(...), password: str = Form(...)):
    flag = os.getenv("FLAG", "CTF{dummy_flag}")
    if USERS.get(username) == password:
        encoded_flag = base64.b64encode(flag.encode()).decode()
        html = """
        <html>
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
    background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)),
        url('/static/images/hero-bg.jpg') center/cover no-repeat;
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

.product-card img {
    width        : 100%;
    height       : 200px;
    object-fit   : cover;
    border-radius: 5px;
    margin-bottom: 1rem;
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

/* Meme Image for Debug or Branding */
img[alt="meme image"] {}
        </style>
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

               <h1 style="margin-left: 500px;">ACCESS GRANTED</h1>
            <img src="/static/images/flag.png" alt="flag" style="margin-left: 500px;" />

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

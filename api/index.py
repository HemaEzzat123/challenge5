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

               <h1>ACCESS GRANTED</h1>
            <img src="/static/flag.png" alt="flag" />

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

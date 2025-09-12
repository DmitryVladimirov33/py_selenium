from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Приветствие</title>
        </head>
        <body>
            <h1>Введите ваше имя и фамилию</h1>
            <form action="/greet" method="post">
                <input type="text" name="name" placeholder="Ваше имя" required>
                <input type="text" name="surname" placeholder="Ваша фамилия" required>
                <button type="submit">Приветствовать</button>
            </form>
        </body>
    </html>
    """


@app.post("/greet", response_class=HTMLResponse)
async def greet(name: str = Form(...), surname: str = Form(...)):
    return f"<h1>Привет, {name} {surname}!</h1> <a href='/'>Назад</a>"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

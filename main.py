from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

# Создаем приложение FastAPI
app = FastAPI()

# Указываем путь к статическим файлам
app.mount("/static", StaticFiles(directory="static"), name="static")

# Загружаем шаблоны из папки 'templates'
templates = Jinja2Templates(directory="templates")

# Чтение данных о продуктах из JSON-файла
products = [
    {
        "title": "Кредитная карта",
        "description": "Удобная кредитная карта с кэшбэком до 5%.",
        "image": "/static/images/product1.jpg",
        "link": "https://example.com/product1"
    },
    {
        "title": "Депозит",
        "description": "Высокодоходный депозит с процентной ставкой до 7%.",
        "image": "/static/images/product2.jpg",
        "link": "https://example.com/product2"
    },
    {
        "title": "Ипотека",
        "description": "Выгодная ипотека от ведущих банков страны.",
        "image": "/static/images/product3.jpg",
        "link": "https://example.com/product3"
    }
]

# Чтение текстов из файла text.json
texts = {
    "main":"Мы реально крутые ребята",
    "about":"Не ну работайте с нами"
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Передача данных о продуктах и текстах в шаблон
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "products": products,
            "about_us": texts['main'],
            "why_work_with_us": texts['about']
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
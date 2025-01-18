from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db import DateBase
import json

# Создаем приложение FastAPI
app = FastAPI()

# Указываем путь к статическим файлам
app.mount("/static", StaticFiles(directory="static"), name="static")

# Загружаем шаблоны из папки 'templates'
templates = Jinja2Templates(directory="templates")

#Подключение к базеданых
products = DateBase()

texts = {
    "main":"Мы реально крутые ребята",
    "about":"Не ну работайте с нами"
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    print(products.get_products())
    # Передача данных о продуктах и текстах в шаблон
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "products": products.get_products(),
            "about_us": texts['main'],
            "why_work_with_us": texts['about']
        }
    )

if __name__ == "__main__":
    import uvicorn
    config = uvicorn.Config("main:app", port=8000, log_level="info", reload=True, host="0.0.0.0")
    server = uvicorn.Server(config)
    server.run()
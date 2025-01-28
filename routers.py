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
    "main":"Мы – команда энтузиастов, чья миссия заключается в том, чтобы помогать людям находить лучшие банковские продукты. Мы тщательно анализируем рынок, сравниваем условия и предлагаем только те решения, которые действительно соответствуют вашим потребностям. Будь то кредит, вклад или дебетовая карта – вы всегда можете рассчитывать на нашу помощь в выборе оптимального варианта.",
    "about":"Работать с нами – это значит выбрать надежность и профессионализм. Наши знания и опыт позволяют нам предлагать вам самые выгодные условия, а индивидуальный подход гарантирует, что каждый клиент получит именно тот продукт, который идеально соответствует его финансовым целям. Вместе с нами вы сможете уверенно планировать свое будущее, зная, что ваши финансы в надежных руках."
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

from db import DateBase

base = DateBase()
for i in range(int(input("Сколько будем добавлять: "))):
    print(f"Делаем {i+1}")
    title = input("Ведите название: ")
    desk = input("Ведите описание: ")
    link = input("Отправте сылку: ")
    image = f"/static/images/{input("Название банера или картинки: ")}.jpg"
    base.add_product(title, desk, link, image)

import os
from dotenv import load_dotenv
load_dotenv()
vk_token = os.getenv("my_token")
vk__token = vk_token[:5] + "*" * (len(vk_token) - 5)
print(vk__token)
# print(vk_token)
# Junior: Создать БОТА и файл .env. Записать туда BOT_TOKEN=ваш_токен.

# Middle: Написать код на Python: загрузить .env, считать токен в переменную и вывести его в консоль, заменив все символы кроме первых 5 на звездочки *****.

# Senior: Создать файл .gitignore, добавить туда .env. Инициализировать git init и проверить через git status, что "сейф" невидим для Гитхаба.


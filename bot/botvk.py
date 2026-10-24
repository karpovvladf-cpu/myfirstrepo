import os
from vkbottle.bot import Bot
from vkbottle.bot import Message
from dotenv import load_dotenv
import random
load_dotenv()

vk_token = os.getenv("my_token")
bot = Bot(token=vk_token)


@bot.on.message()
async def hello_handler(message: Message):
    if message.text == "секрет" or message.text == "пароль":
        await message.answer("Я никому не скажу! 🤫")
    else:
        await message.answer(message.text) 
    
        




bot.run()


# Уровень Junior: "Бот-повторялка с характером"
# ● Сделайте так, чтобы бот повторял всё, что написал юзер (Эхо-бот).
# ● НО! Если юзер написал слово "секрет" или "пароль", бот должен ответить: "Я никому не скажу! 🤫" и НЕ повторять это слово.

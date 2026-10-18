import os
from vkbottle.bot import Bot
from vkbottle.bot import Message
from dotenv import load_dotenv
import random
load_dotenv()

vk_token = os.getenv("my_token")
bot = Bot(token=vk_token)


@bot.on.message(text = "бросок")
async def hello_handler(message: Message):
    rand = random.randint(1,6)
    await message.answer(f"выпало: {rand}")


bot.run()
import os
from dotenv import load_dotenv
load_dotenv()
vk_token = os.getenv("my_token")

if vk_token:
    vk__token = vk_token[:5] + "*" * (len(vk_token) - 5)
    print(vk__token)
else:
    print("првоерьте .env")

import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    403829853
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

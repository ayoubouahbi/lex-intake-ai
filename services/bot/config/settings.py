import os
from dotenv import load_dotenv

load_dotenv("../api/.env")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

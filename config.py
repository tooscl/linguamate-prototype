import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
YC_OAUTH_TOKEN = os.getenv("YC_OAUTH_TOKEN")
YC_FOLDER_ID = os.getenv("YC_FOLDER_ID")

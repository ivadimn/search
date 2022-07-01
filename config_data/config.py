import os
from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Environment variables not loaded, file .env not found")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
HEALTH_URL = os.getenv("HEALTH_URL")
HEALTH_BASE_URL = os.getenv("HEALTH_BASE_URL")
USER_AGENT = os.getenv("USER_AGENT")
COMMANDS = (
    ('start', "Start bot"),
    ('foods', "Search food's info"),
    ('help', "Show help")
)
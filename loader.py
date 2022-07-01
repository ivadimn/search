from config_data import config
from aiogram import Bot, Dispatcher
from repositories.user_repository import get_users

users = get_users()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

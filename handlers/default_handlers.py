from aiogram import types
from loader import dp, users, bot
from model_data.model import User
from pprint import pprint
from repositories.user_repository import UserRepository


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    user = users.get(message.from_user.id)
    if user is None:
        if message.from_user.language_code.lower() == "ru":
            locale = "ru_RU"
        else:
            locale = "en_US"
        user = User(message.from_user.id, message.chat.full_name, locale)
        UserRepository().insert([user])
    msg = "Hello {0}, welcome to foods info bot".format(
                        user.name)
    pprint(user)
    await bot.send_message(message.chat.id, msg)

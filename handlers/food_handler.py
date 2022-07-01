from aiogram import types
from loader import dp, users, bot
from model_data.model import User, Food


@dp.message_handler(commands=["foods"])
async def cmd_foods(message: types.Message) -> None:
    await message.reply("Введите название продукта")


@dp.message_handler(content_types=["text"])
async def cmd_foods(message: types.Message) -> None:
    await message.reply("Будем искать: {0}".format(message.text))

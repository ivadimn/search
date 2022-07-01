from aiogram import Bot, Dispatcher, executor, types
from loader import dp, bot
from aiogram.types import BotCommand
from config_data.config import COMMANDS
from utils.functions import set_commands
import handlers
from model_data.model import User, Food
from repositories.food_repository import FoodRepository
from generators import sql


async def on_startup(_):
    await bot.set_my_commands(
        [BotCommand(*command) for command in COMMANDS]
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    #parce_food()
    #foods = FoodRepository().select((60,))
    #print(foods)
    #print(sql.gen_select_all(User, "users"))
    #print(sql.gen_insert(User, "users", autoincrement=False))




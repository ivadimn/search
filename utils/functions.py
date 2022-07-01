from typing import List
from aiogram import Bot
from aiogram.types import BotCommand
from config_data.config import COMMANDS
import re
import json
import csv


def write_to_csv(file_name: str, header: List[str], rows: List[tuple]) -> None:
    with open(file_name, "w", encoding="UTF-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def write_html_file(file_name: str, data: str) -> None:
    with open(file_name, "w", encoding="UTF-8") as f:
        f.write(data)


def read_html_file(file_name: str) -> str:
    with open(file_name, "r", encoding="UTF-8") as f:
        data = f.read()
    return data


def replace_symbols(s: str) -> str:
    repl = re.sub("[,.';: ]", "_", s)
    return repl


def set_commands(bot: Bot):
    bot.set_my_commands(
        [BotCommand(*command) for command in COMMANDS]
    )

import csv
import requests
from bs4 import BeautifulSoup
from config_data import config
import os
import re
import time
from utils.functions import write_html_file, read_html_file, write_to_csv, replace_symbols
from repositories.food_group_repository import FoodGroupRepository
from repositories.food_repository import FoodRepository

from pprint import pprint
from model_data.model import FoodGroup, Food

food_groups = "food_groups.html"
food_groups_csv = "food_groups.csv"

headers = {
        "Accept": "*/*",
        "User-Agent": config.USER_AGENT
    }


def get_group_products(url: str, group_name: str) -> list:
    html_file = "data/{0}.{1}".format(group_name, "html")
    csv_file = "data/{0}.{1}".format(group_name, "csv")
    if not os.path.exists(html_file):
        response = requests.get(url, headers=headers)
        src = response.text
        write_html_file(html_file, src)
    else:
        src = read_html_file(html_file)

    soup = BeautifulSoup(src, "lxml")
    table = soup.find("table", class_ = "uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed")
    if table is None:
        print("{0} - не найдено!".format(group_name))
        return []
    heads = table.find("thead").find("tr").find_all("th")
    columns = list()
    for head in heads:
        columns.append(head.text)
    columns.append("url")
    rows = list()
    trs = table.find("tbody").find_all("tr")
    for tr in trs:
        ths = tr.find_all("td")
        a = ths[0].find("a")
        prod_name = a.text.replace(",", "")
        url = "{0}{1}".format(config.HEALTH_BASE_URL, a.get("href"))
        kkal = re.sub("[А-Яа-я ]", "", ths[1].text).replace(",", ".")
        squirrels = re.sub("[А-Яа-я ]", "", ths[2].text).replace(",", ".")
        fats = re.sub("[А-Яа-я ]", "", ths[3].text).replace(",", ".")
        carbos = re.sub("[А-Яа-я ]", "", ths[4].text).replace(",", ".")
        rows.append((prod_name, kkal, squirrels, fats, carbos, url))
    write_to_csv(csv_file, columns, rows)
    print("Created file: {0}".format(csv_file))
    return []


def insert_into_db() -> None:
    groups = list()
    with open("data/{0}".format("food_groups.csv"), "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            name = row[0].replace("_", " ").replace("  ", ", ")
            groups.append(FoodGroup(0, name, row[1]))
    rep = FoodGroupRepository()
    rep.insert(groups)
    print("inserted")


def insert_food(file_name: str, group: str) -> None:
    foods = list()
    rep = FoodGroupRepository()
    if not os.path.exists(file_name):
        return
    param = tuple([group])
    fgs = rep.select(param)
    print(fgs)
    with open(file_name, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            food = Food(0, row[0], fgs[0].id, float(row[1]), float(row[2]),
                        float(row[3]), float(row[4]), row[5])
            foods.append(food)
            print(row)
        print("-" * 50)
    frep = FoodRepository()
    frep.insert(foods)
    print("inserted")


def parce_food() -> None:

    if not os.path.exists("data/{0}".format(food_groups)):
        response = requests.get(config.HEALTH_URL, headers=headers)
        src = response.text
        write_html_file("data/{0}".format(food_groups), src)
    else:
        src = read_html_file("data/{0}".format(food_groups))

    soup = BeautifulSoup(src, "lxml")
    groups_link = soup.find_all("a", class_="mzr-tc-group-item-href")
    columns_names = ["group_name", "url"]
    rows = list()
    for link in groups_link:
        repl_name = replace_symbols(link.text)
        rows.append((repl_name, "{0}{1}".format(config.HEALTH_BASE_URL, link.get("href"))))
    pprint(rows)
    write_to_csv("data/{0}".format(food_groups_csv), columns_names, rows)
    for row in rows:
        get_group_products(row[1], row[0])
        time.sleep(0.5)


def insert_group_foods() -> None:
    with open("data/{0}".format(food_groups_csv), "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            file_name = "data/{0}.{1}".format(row[0], "csv")
            name = row[0].replace("_", " ").replace("  ", ", ")
            insert_food(file_name, name)

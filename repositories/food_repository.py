from sqlite3 import Error
from model_data.model import Food
from typing import List
from repositories.repository import Repository
from db.data_base import Db
from generators import sql


class FoodRepository(Repository):

    def select(self, params: tuple) -> List[Food]:
        if len(params) > 0:
            sql_select = sql.gen_select_by_id(Food, "foods", "group_id")
        else:
            sql_select = sql.gen_select_all(Food, "foods")
        rows = Db.select(sql_select, params)
        foods = list()
        for row in rows:
            foods.append(Food(*row))
        return foods

    def insert(self, entities: List[Food]) -> int:
        sql_insert = sql.gen_insert(Food, "foods")
        try:
            list_values = []
            for food in entities:
                list_values.append((food.group_id, food.name, food.kkal, food.belki,
                                    food.fats, food.ugl, food.url))
            row_id = Db.insert(sql_insert, list_values)
            return row_id
        except Error as err:
            print(str(err))
            return -1

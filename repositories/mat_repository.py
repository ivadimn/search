from sqlite3 import Error
from model_data.model import Mat
from typing import List
from repositories.repository import Repository
from db.data_base import Db
from generators import sql

class MatRepository(Repository):

    def select(self, params: tuple) -> List[Mat]:
        if len(params) > 0:
            sql_select = sql.gen_select_by_id(Mat, "black_list", "id")
        else:
            sql_select = sql.gen_select_all(Mat, "black_list")
        rows = Db.select(sql_select, params)
        mat_list = list()
        for row in rows:
            mat_list.append(Mat(*row))
        return mat_list

    def insert(self, entities: List[Mat]) -> int:
        pass
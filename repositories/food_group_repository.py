from sqlite3 import Error
from model_data.model import FoodGroup
from typing import List
from repositories.repository import Repository
from contracts.db_contracts import FoodGroupsContract
from db.data_base import Db


class FoodGroupRepository(Repository):
    _sql_select_all = "SELECT {0}, {1}, {2} FROM {3} ".format(
        FoodGroupsContract.Columns.ID,
        FoodGroupsContract.Columns.GROUP_NAME,
        FoodGroupsContract.Columns.URL,
        FoodGroupsContract.TABLE_NAME
    )

    _sql_select_one = "SELECT {0}, {1}, {2} FROM {3} WHERE {4}=?".format(
        FoodGroupsContract.Columns.ID,
        FoodGroupsContract.Columns.GROUP_NAME,
        FoodGroupsContract.Columns.URL,
        FoodGroupsContract.TABLE_NAME,
        FoodGroupsContract.Columns.GROUP_NAME
    )

    _sql_insert = "INSERT INTO {0}({1}, {2}) VALUES(?, ?) ".\
        format(FoodGroupsContract.TABLE_NAME,
               FoodGroupsContract.Columns.GROUP_NAME,
               FoodGroupsContract.Columns.URL)

    def select(self, params: tuple) -> List[FoodGroup]:
        if len(params) > 0:
            sql = self._sql_select_one
        else:
            sql = self._sql_select_all
        groups = list()
        rows = Db.select(sql, params)
        for row in rows:
            groups.append(FoodGroup(row[0], row[1], row[2]))
        return groups

    def insert(self, entities: List[FoodGroup]) -> int:
        try:
            list_values = []
            for group in entities:
                list_values.append((group.name, group.url))
            Db.insert(self._sql_insert, list_values)
            return 1
        except Error as err:
            print(str(err))
            return -1

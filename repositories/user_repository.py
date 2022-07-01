from sqlite3 import Error
from model_data.model import User
from typing import List
from repositories.repository import Repository
from db.data_base import Db
from generators import sql


class UserRepository(Repository):

    def select(self, params: tuple) -> List[User]:
        if len(params) > 0:
            sql_select = sql.gen_select_by_id(User, "users", "id")
        else:
            sql_select = sql.gen_select_all(User, "users")
        rows = Db.select(sql_select, params)
        user_list = list()
        for row in rows:
            user_list.append(User(*row))
        return user_list

    def insert(self, entities: List[User]) -> int:
        try:
            list_values = []
            for user in entities:
                list_values.append((user.id, user.name, user.locale))
            sql_insert = sql.gen_insert(User, "users", autoincrement=False)
            row_id = Db.insert(sql_insert, list_values)
            return row_id
        except Error as err:
            print(str(err))
            return -1


def get_users() -> dict:
    user_list = UserRepository().select(())
    users_dict = {user.id: user for user in user_list}
    return users_dict

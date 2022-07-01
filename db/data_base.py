import sqlite3


class Db:

    @classmethod
    def select(cls, sql: str, params: tuple) -> list:
        with sqlite3.connect("data.db") as conn:
            if len(params) > 0:
                cursor = conn.execute(sql, params)
            else:
                cursor = conn.execute(sql)
        return cursor.fetchall()

    @classmethod
    def insert(cls, sql: str, params: list) -> int:
        with sqlite3.connect("data.db") as conn:
            if len(params) > 0:
                for ps in params:
                    cursor = conn.execute(sql, ps)
            else:
                cursor = conn.execute(sql)
        return cursor.lastrowid

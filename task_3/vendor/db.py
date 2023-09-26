import os

import psycopg2

from second_part.port import DatabasePort
import dotenv
dotenv.load_dotenv()

class PostgresDatabaseAdapter(DatabasePort):
    def __init__(self):
        self._dbname = os.environ.get("postgres_db")
        self._user = os.environ.get("postgres_user")
        self._password = os.environ.get("postgres_password")
        self._host = os.environ.get("postgres_host")
        self._port = os.environ.get("postgres_port")
        self._connection = None

    def _connect(self):
        try:
            print("connect", self._dbname, self._user, self._password, self._host, self._port)
            if self._connection is None or self._connection.closed != 0:
                self._connection = psycopg2.connect(
                    dbname=self._dbname,
                    user=self._user,
                    password=self._password,
                    host=self._host,
                    port=self._port
                )
            return self._connection
        except Exception as error:
            print(error, error.with_traceback(error.__traceback__))
            return None

    def _disconnect(self):
        try:
            if self._connection is not None and self._connection.closed == 0:
                self._connection.close()
        except Exception as error:
            print(f"Database: {error.with_traceback()}")

    def find_all(self, table_name):
        self._connection = self._connect()
        print("find")
        if self._connection:
            cur = self._connection.cursor()

            cur.execute(f"SELECT * FROM {table_name}")
            result = cur.fetchall()
            print(result)

            self._connection.close()
            self._disconnect()
            return result
        print("some_error")
        return None

    def find_by_id(self, table_name, id):
        self._connection = self._connect()
        if self._connection:
            cur = self._connection.cursor()
            id = "'" + id + "'"
            cur.execute(f'SELECT * FROM {table_name} WHERE addr_ipv4={id}')

            result = cur.fetchone()
            self._connection.close()
            self._disconnect()
            return result
        return None

    def find_by_param(self, table_name, conditional_data: dict):
        self._connection = self._connect()
        if self._connection:
            cur = self._connection.cursor()
            data = "'" + conditional_data['data'] + "'"
            cur.execute(f'SELECT * FROM {table_name} WHERE {conditional_data["column"]} = {data}')

            result = cur.fetchall()
            self._connection.close()
            self._disconnect()
            return result
        return None

    def create(self, table_name, data: list):
        self._connection = self._connect()
        if self._connection:
            cur = self._connection.cursor()
            data = ", ".join(["'" + str(item) + "'" for item in data])
            cur.execute(f'INSERT INTO {table_name} VALUES ({data}) ON CONFLICT DO NOTHING')

            self._connection.commit()
            self._connection.close()
            self._disconnect()
            return cur.rowcount
        return None

    def update(self, table_name, conditional_data: dict, replacement_data: dict):
        self._connection = self._connect()
        if self._connection:
            cur = self._connection.cursor()

            conditional = "'" + conditional_data['data'] + "'"
            replace = "'" + replacement_data['data'] + "'"
            print(conditional, replace)

            cur.execute(f"UPDATE {table_name} set {replacement_data['column']} = {replace} where {conditional_data['column']} = {conditional}")

            self._connection.commit()
            self._connection.close()
            self._disconnect()
        return None

    def delete(self, table_name, conditional_data: dict):
        self._connection = self._connect()
        if self._connection:
            # Удаление записи из таблицы по id
            cur = self._connection.cursor()
            cur.execute(f"DELETE FROM {table_name} WHERE id=?", (id,))
            cur.commit()
            cur.close()
            self._disconnect()
        return None


# if __name__ == "__main__":
#     ex = PostgresDatabaseAdapter()
#     # ex.create("bridges_fetched", ["192.1321.322", "google33", 1])
#     # print(ex.find_all("bridges_fetched"))
#     # ex.update(table_name="bridges_fetched",
#     #           replacement_data={"column": "source_data", "data": "tg"},
#     #           conditional_data={"column": "addr_ipv4", "data": "192.1321.31"})
#     print(ex.find_by_param("bridges_fetched", conditional_data={"column": "addr_ipv4", "data": "192.1321.391"}))

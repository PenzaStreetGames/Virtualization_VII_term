from contextlib import closing

import psycopg2
import psycopg2.extras

from entities import Fruit


class DbConnector:
    def __init__(
            self, dbname: str, user: str, password: str, host: str, port: int
    ):
        self.credentials = {
            'dbname': dbname, 'user': user, 'password': password, 'host': host,
            'port': port
        }

    def create_fruit(self, fruit: Fruit):
        psycopg2.extras.register_uuid()
        with closing(psycopg2.connect(**self.credentials)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO fruit(uid, name, color) VALUES (%s, %s, %s);',
                    (str(fruit.uid), fruit.name, fruit.color)
                )
                conn.commit()

    def get_fruits(self) -> list[dict]:
        psycopg2.extras.register_uuid()
        with closing(psycopg2.connect(**self.credentials)) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'SELECT * FROM fruit;'
                )
                rows = cursor.fetchall()
        return rows

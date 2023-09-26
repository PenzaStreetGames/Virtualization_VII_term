import dataclasses
import uuid

from entities import Fruit
from postgre import DbConnector


class Controller:
    def __init__(self, db_connector: 'DbConnector'):
        self.db_connector = db_connector

    def create_fruit(self, data: dict) -> dict:
        fruit = Fruit(name=data['name'], color=data['color'], uid=uuid.uuid4())
        self.db_connector.create_fruit(fruit)
        return dataclasses.asdict(fruit)

    def get_fruits(self) -> list[dict]:
        return [
            dataclasses.asdict(Fruit(name=name, color=color, uid=uid))
            for uid, name, color in self.db_connector.get_fruits()
        ]

import dataclasses
from uuid import UUID


@dataclasses.dataclass
class Fruit:
    name: str
    color: str
    uid: UUID

from typing import Dict, Iterable, List, Optional

from app.models.object import DomainObject


def _default_objects() -> Iterable[DomainObject]:
    return [
        DomainObject(id=1, name="Anemometer", description="Wind speed sensor"),
        DomainObject(id=2, name="Barometer", description="Atmospheric pressure sensor"),
    ]


class InMemoryObjectRepository:
    def __init__(self, initial_objects: Optional[Iterable[DomainObject]] = None) -> None:
        objects = list(initial_objects or _default_objects())
        self._objects: Dict[int, DomainObject] = {obj.id: obj for obj in objects}
        self._next_id = max((obj.id for obj in objects), default=0) + 1

    def list(self) -> List[DomainObject]:
        return list(self._objects.values())

    def get(self, object_id: int) -> Optional[DomainObject]:
        return self._objects.get(object_id)

    def create(self, name: str, description: str) -> DomainObject:
        obj = DomainObject(id=self._next_id, name=name, description=description)
        self._objects[obj.id] = obj
        self._next_id += 1
        return obj

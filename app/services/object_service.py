from typing import List, Optional

from app.models.object import DomainObject
from app.repositories.object_repository import InMemoryObjectRepository


class ObjectService:
    def __init__(self, repository: InMemoryObjectRepository) -> None:
        self.repository = repository

    def list_objects(self) -> List[DomainObject]:
        return self.repository.list()

    def get_object(self, object_id: int) -> Optional[DomainObject]:
        return self.repository.get(object_id)

    def create_object(self, name: str, description: str) -> DomainObject:
        return self.repository.create(name=name, description=description)

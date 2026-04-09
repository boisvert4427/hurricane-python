from dataclasses import dataclass


@dataclass(frozen=True)
class DomainObject:
    id: int
    name: str
    description: str

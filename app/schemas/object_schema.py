from typing import Any, Dict

from app.models.object import DomainObject


class ValidationError(ValueError):
    pass


def validate_object_payload(payload: Any) -> Dict[str, str]:
    if not isinstance(payload, dict):
        raise ValidationError("JSON body must be an object")

    name = str(payload.get("name", "")).strip()
    description = str(payload.get("description", "")).strip()

    if not name:
        raise ValidationError("Field 'name' is required")
    if not description:
        raise ValidationError("Field 'description' is required")

    return {"name": name, "description": description}


def serialize_object(obj: DomainObject) -> Dict[str, Any]:
    return {
        "id": obj.id,
        "name": obj.name,
        "description": obj.description,
    }

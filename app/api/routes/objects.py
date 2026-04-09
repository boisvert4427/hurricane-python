from flask import Blueprint, current_app, jsonify, request

from app.schemas.object_schema import ValidationError, serialize_object, validate_object_payload


bp = Blueprint("objects", __name__)


def get_object_service():
    return current_app.extensions["object_service"]


@bp.get("", strict_slashes=False)
def list_objects():
    objects = get_object_service().list_objects()
    return jsonify([serialize_object(obj) for obj in objects])


@bp.get("/<int:object_id>")
def get_object(object_id: int):
    obj = get_object_service().get_object(object_id)
    if obj is None:
        return jsonify({"error": "Object not found"}), 404
    return jsonify(serialize_object(obj))


@bp.post("", strict_slashes=False)
def create_object():
    payload = request.get_json(silent=True)
    try:
        data = validate_object_payload(payload)
    except ValidationError as exc:
        return jsonify({"error": str(exc)}), 400

    obj = get_object_service().create_object(**data)
    return jsonify(serialize_object(obj)), 201

from flask import Flask, jsonify

from app.api import register_blueprints
from app.config import Config
from app.repositories.object_repository import InMemoryObjectRepository
from app.services.object_service import ObjectService


def create_app(config_object: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.extensions["object_service"] = ObjectService(InMemoryObjectRepository())

    register_blueprints(app)

    @app.get("/")
    def index():
        return jsonify({"message": f"{app.config['APP_NAME']} is running"})

    return app

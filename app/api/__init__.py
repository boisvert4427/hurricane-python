from flask import Flask

from app.api.routes.health import bp as health_bp
from app.api.routes.objects import bp as objects_bp


def register_blueprints(app: Flask) -> None:
    api_prefix = app.config["API_PREFIX"]
    app.register_blueprint(health_bp, url_prefix=api_prefix)
    app.register_blueprint(objects_bp, url_prefix=f"{api_prefix}/objects")

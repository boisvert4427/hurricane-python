class Config:
    APP_NAME = "Hurricane Python API"
    API_PREFIX = "/api/v1"
    TESTING = False


class TestingConfig(Config):
    TESTING = True

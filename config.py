import os


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2


class DevelopmentConfig(Config):
    DEBUG = True
    HDB_TRACE = 1
    CORS_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    HDB_TRACE = 0


app_config = {
    "DEVELOPMENT": DevelopmentConfig,
    "PRODUCTION": ProductionConfig
}

from flask import Flask
from flask_cors import CORS

from app.doctor.controller import doctor_visit_controller
from app.ethnicity.controller import ethnicity_controller
from app.main.controller import main_controller
from app.worldwide.controller import worldwide_controller
from app.usa.controller import usa_controller
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(worldwide_controller, url_prefix='/api/world')
    app.register_blueprint(usa_controller, url_prefix='/api/usa')
    app.register_blueprint(ethnicity_controller, url_prefix='/api/usa/ethnicity')
    print(f"Started app with config: {config_name}")
    return app

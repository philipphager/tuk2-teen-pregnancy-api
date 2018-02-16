from flask import Flask
from flask_cors import CORS

from app.education.controller import education_controller
from app.ethnicity.controller import ethnicity_controller
from app.funding.chart_controller import funding_chart_controller
from app.funding.controller import funding_controller
from app.main.controller import main_controller
from app.religion.controller import religion_controller
from app.usa.controller import usa_controller
from app.worldwide.controller import worldwide_controller
from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(worldwide_controller, url_prefix='/api/world')
    app.register_blueprint(usa_controller, url_prefix='/api/usa')
    app.register_blueprint(ethnicity_controller, url_prefix='/api/usa/ethnicity')
    app.register_blueprint(education_controller, url_prefix='/api/usa/education')
    app.register_blueprint(funding_controller, url_prefix='/api/usa/funding')
    app.register_blueprint(religion_controller, url_prefix='/api/usa/religion')
    app.register_blueprint(funding_chart_controller, url_prefix='/api/funding')
    print(f"Started app with config: {config_name}")
    return app

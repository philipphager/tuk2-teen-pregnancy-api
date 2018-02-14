from flask import Blueprint, jsonify, request

from app.ethnicity.service import get_teen_pregnancy_by_ethnicity

ethnicity_controller = Blueprint('ethnicity', __name__)


@ethnicity_controller.route('/')
def birth_rate_usa_per_year_and_ethnicity():
    year = request.args.get('year', 2003, int)
    data = get_teen_pregnancy_by_ethnicity(year)
    return jsonify(data)

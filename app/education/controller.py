from flask import Blueprint, jsonify, request

from app.education.service import get_teen_pregnancy_by_education

education_controller = Blueprint('education', __name__)


@education_controller.route('/')
def birth_rate_usa_per_year_and_education():
    year = request.args.get('year', 1995, int)
    data = get_teen_pregnancy_by_education(year)
    return jsonify(data)

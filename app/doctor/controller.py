from flask import Blueprint, jsonify, request

from app.doctor.service import get_doctor_visit_count, get_doctor_visit_count_relative_to_state

doctor_visit_controller = Blueprint('doctor', __name__)


@doctor_visit_controller.route('/')
def doctor_visit_count():
    count_type = request.args.get('type', 'absolute', str)
    start_year = request.args.get('startYear', 1970, int)
    end_year = request.args.get('endYear', 2017, int)
    is_male = request.args.get('isMale') == 'true'
    is_female = request.args.get('isFemale') == 'true'

    if count_type == 'relative':
        visit_count = get_doctor_visit_count_relative_to_state(start_year, end_year, is_male, is_female)
    else:
        visit_count = get_doctor_visit_count(start_year, end_year, is_male, is_female)
    return jsonify(visit_count)

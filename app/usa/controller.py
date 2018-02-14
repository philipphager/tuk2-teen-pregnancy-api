from flask import Blueprint, request, jsonify

from app.usa.service import get_teen_pregnancy_by_state

usa_controller = Blueprint('usa', __name__)


@usa_controller.route('/')
def average_bmi():
    year = request.args.get('year', 1995, int)
    bmi = get_teen_pregnancy_by_state(year)
    return jsonify(bmi)

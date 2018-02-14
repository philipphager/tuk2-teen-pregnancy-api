from flask import Blueprint, request, jsonify

from app.usa.service import get_teen_pregnancy_by_state

usa_controller = Blueprint('usa', __name__)


@usa_controller.route('/')
def birth_rate_usa_per_year():
    year = request.args.get('year', 1995, int)
    data = get_teen_pregnancy_by_state(year)
    return jsonify(data)

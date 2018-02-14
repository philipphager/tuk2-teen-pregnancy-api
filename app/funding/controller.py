from flask import Blueprint, jsonify, request

from app.funding.service import get_funding_by_state

funding_controller = Blueprint('funding', __name__)


@funding_controller.route('/')
def funding_per_state_and_year():
    year = request.args.get('year', 2003, int)
    data = get_funding_by_state(year)
    return jsonify(data)

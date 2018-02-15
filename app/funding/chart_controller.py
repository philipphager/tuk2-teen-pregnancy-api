from flask import Blueprint, jsonify, request

from app.funding.chart_service import get_funding_aggregated_by_state

funding_chart_controller = Blueprint('funding_chart', __name__)


@funding_chart_controller.route('/')
def funding_per_state_and_year():
    default_states = ['01']
    start_year = request.args.get('startYear', 2003, int)
    end_year = request.args.get('endYear', 2016, int)
    states = request.args.getlist('state', str)

    if not states:
        states = default_states

    data = get_funding_aggregated_by_state(start_year, end_year, states)
    return jsonify(data)

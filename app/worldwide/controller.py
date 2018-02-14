from flask import Blueprint, jsonify, request

from app.worldwide.service import get_teen_pregnancy_world_wide

worldwide_controller = Blueprint('world', __name__)


@worldwide_controller.route('/')
def birth_rate_worldwide():
    start_year = request.args.get('startYear', 1970, int)
    end_year = request.args.get('endYear', 2017, int)
    countries = request.args.get('countries') == []
    data = get_teen_pregnancy_world_wide(start_year, end_year, countries)
    return jsonify(data)

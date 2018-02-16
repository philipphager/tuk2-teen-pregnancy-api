from flask import Blueprint, jsonify

from app.religion.service import get_religiousness_by_state

religion_controller = Blueprint('religion', __name__)


@religion_controller.route('/')
def religiousness_by_state():
    data = get_religiousness_by_state()
    return jsonify(data)

from flask import Blueprint, render_template

main_controller = Blueprint('main', __name__)


@main_controller.route('/', defaults={'path': ''})
@main_controller.route('/<path:path>')
def index(path):
    return render_template('index.html')

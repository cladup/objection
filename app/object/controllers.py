from flask import Blueprint


object_page = Blueprint('objects', __name__)


@object_page.route('/objects', methods=['GET'])
def list():
    return "Hello, World!"


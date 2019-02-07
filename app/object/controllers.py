from flask import Blueprint


object_page = Blueprint('objects', __name__)


@image_page.route('/objects', methods=['GET'])
def objects():
    return "Hello, World!"


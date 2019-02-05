from flask import Blueprint


image_page = Blueprint('images', __name__)


@image_page.route('/images', methods=['GET'])
def images():
    return "Hello, World!"


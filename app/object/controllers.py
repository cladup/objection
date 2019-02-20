from flask import Blueprint, request, Response
from app.util import uploader


object_page = Blueprint('objects', __name__)


@object_page.route('/objects', methods=['POST'])
def create():
    """
    Upload object to cloud storage
    """
    if 'graphic_model' not in request.files:
        return Response("graphic_model is empty", 400)
    graphic_model = request.files.get('graphic_model')
    if graphic_model.filename == '':
        return Response("No selected file", 400)
    if not uploader.allowed_file(graphic_model.filename):
        return Response("File extension not allowed", 400)
    # Upload and save to database
    # TODO: Save to database
    return uploader.upload(graphic_model).name


@object_page.route('/objects', methods=['GET'])
def get():
    """
    FIXME: Create debug purpose file input UI
    """
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=graphic_model>
      <input type=submit value=Upload>
    </form>
    '''


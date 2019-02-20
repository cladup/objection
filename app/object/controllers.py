from flask import Blueprint, request, Response, jsonify
from app.util import uploader
from app.object.models import Object
from app.object.json_schemas import ObjectSchema


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
    uploaded_blob = uploader.upload(graphic_model)
    file_type = uploader.file_extension(uploaded_blob.name)
    new_object = Object(uploaded_blob.name, uploaded_blob.name, file_type)
    new_object.save()
    schema = ObjectSchema()
    result = { 'data': { 'object': schema.dumps(new_object) } }
    return jsonify(result)


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


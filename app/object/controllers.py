from flask import Blueprint, request, Response, jsonify, abort
from app.util import uploader
from app.object.models import *
from app.object.json_schemas import ObjectSchema


object_page = Blueprint('objects', __name__)


@object_page.route('/v1/objects/<alias>', methods=['GET'])
def get(alias):
    """
    Get object by alias
    """
    found_object = Object.query.filter_by(alias=alias, status=STATUS_ALIASED).first()
    schema = ObjectSchema()
    #return schema.dumps(found_object)
    return alias


@object_page.route('/v1/objects', methods=['POST'])
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
    return schema.dumps(new_object)


@object_page.route('/v1/objects/<name>', methods=['PATCH'])
def alias(name):
    """
    Alias object name
    """
    alias = request.get_json().get('alias')
    if alias == None:
        return Response("Alias is missing", 400)
    aliasing_object = Object.query.filter_by(name=name, status=STATUS_STAGING).first()
    if aliasing_object == None:
        abort(404)
    aliasing_object.alias(alias)
    schema = ObjectSchema()
    return schema.dumps(aliasing_object)


@object_page.route('/v1/objects/<alias>', methods=['DELETE'])
def unalias(alias):
    """
    Unalias object
    """
    unaliasing_object = Object.query.filter_by(alias=alias, status=STATUS_ALIASED).first()
    if unaliasing_object == None:
        abort(404)
    unaliasing_object.unalias()
    schema = ObjectSchema()
    return schema.dumps(unaliasing_object)


from flask import Blueprint, request, Response, jsonify, abort, redirect, make_response
from app.util import uploader
from app.util import blob
from app.object.models import *
from app.object.json_schemas import ObjectSchema


object_page = Blueprint('objects', __name__)


@object_page.route('/api/v1/objects/<component>/<type>/<key>', methods=['GET'])
def get(component, type, key):
    """
    Get object by alias
    Alias spec: {component}/{type}/{key}
    """
    alias = "/".join([component, type, key])
    found_object = Object.query.filter_by(alias_link=alias, status=STATUS_ALIASED).first()
    if found_object == None:
        abort(404)
    return redirect(blob.generate_signed_url(found_object.name))


@object_page.route('/api/v1/objects', methods=['POST'])
def create():
    """
    Upload object to cloud storage
    """
    if 'object_file' not in request.files:
        return Response("object_file is empty", 400)
    object_file = request.files.get('object_file')
    if object_file.filename == '':
        return Response("No selected file", 400)
    if not uploader.allowed_file(object_file.filename):
        return Response("File extension not allowed", 400)
    # Upload and save to database
    uploaded_blob = uploader.upload(object_file)
    file_type = uploader.file_extension(uploaded_blob.name)
    new_object = Object(uploaded_blob.name, uploaded_blob.name, file_type)
    new_object.save()
    schema = ObjectSchema()
    return make_response(schema.dumps(new_object), 201)


@object_page.route('/api/v1/objects/<name>', methods=['PATCH'])
def alias(name):
    """
    Alias object name
    """
    alias = request.get_json().get('alias')
    if alias == None:
        return Response("Alias is missing", 400)
    # Unalias object when alias exists
    aliased_object = Object.query.filter_by(alias_link=alias, status=STATUS_ALIASED).first()
    if aliased_object != None:
        aliased_object.unalias()
    # Alias object
    aliasing_object = Object.query.filter_by(name=name, status=STATUS_STAGING).first()
    if aliasing_object == None:
        abort(404)
    aliasing_object.alias(alias)
    schema = ObjectSchema()
    return schema.dumps(aliasing_object)


@object_page.route('/api/v1/objects/<name>', methods=['DELETE'])
def unalias(name):
    """
    Unalias object
    """
    unaliasing_object = Object.query.filter_by(name=name, status=STATUS_ALIASED).first()
    if unaliasing_object == None:
        abort(404)
    unaliasing_object.unalias()
    schema = ObjectSchema()
    return schema.dumps(unaliasing_object)


import os
import datetime
from google.cloud import storage
from nanoid import generate
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'fbx', 'glb', 'gltf'])


def upload(graphic_object):
    """
    Upload object to cloud storage
    In this app, mostly it'll be fbx, glTF, jpeg
    """
    client = storage.Client.from_service_account_json(os.environ.get('GCP_CREDENTIALS'))
    bucket = client.get_bucket(os.environ.get('BUCKET'))
    # Nano id(Better uuid) + timestamp + file extension
    timestamp = int(datetime.datetime.now().timestamp() * 10**6)
    destination_blob_name = "{}_{}.{}".format(
            generate(size=32),
            str(timestamp),
            _file_extension(secure_filename(graphic_object.filename)))
    blob = bucket.blob(destination_blob_name)
    # TODO: Decide content_type for graphic models
    blob.upload_from_file(graphic_object, content_type=graphic_object.content_type)
    return blob.name


def allowed_file(filename):
    """
    Check whether file extension is allowed
    """
    return '.' in filename and \
           _file_extension(filename) in ALLOWED_EXTENSIONS


def _file_extension(filename):
    """
    Get file extension from filename
    """
    return filename.rsplit('.', 1)[1].lower()


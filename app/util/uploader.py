from google.cloud import storage
from nanoid import generate


def upload(graphic_object):
    """
    Upload object to cloud storage
    In this app, mostly it'll be fbx, glTF, jpeg
    """
    client = storage.Client()
    bucket_name = 'graphic-model-store'
    bucket = client.get_bucket(bucket_name)
    # Nano id(Better uuid) + timestamp
    destination_blob_name = "{}_{}".format(
            generate(size=64),
            str(datetime.datetime.now().timestamp() * 1000))
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(graphic_object)
    return blob.name


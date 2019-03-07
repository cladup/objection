import os
from datetime import datetime, timedelta
from google.cloud import storage


def find(filename):
    """
    Find blob from storage
    """
    client = storage.Client()
    bucket = client.get_bucket(os.environ.get('BUCKET'))
    return bucket.blob(filename)


def generate_signed_url(filename):
    """
    Generate a signed url to access publicly
    """
    found_blob = find(filename)
    expiration = datetime.now() + timedelta(hours=1)
    return found_blob.generate_signed_url(expiration)


from google.cloud import storage


def find(filename):
    """
    Find blob from storage
    """
    client = storage.Client.from_service_account_json(os.environ.get('GCP_CREDENTIALS'))
    bucket = client.get_bucket(os.environ.get('BUCKET'))
    return bucket.blob(filename)


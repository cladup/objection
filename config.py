import os


# Import dotenv
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Set debug runtime environment
DEBUG = True

# Database connection
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "mysql://user:password@db:3306/objection")
SQLALCHEMY_TRACK_MODIFICATIONS = False


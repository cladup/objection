import os


# Import dotenv
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Set debug runtime environment
FLASK_ENV = os.environ.get("FLASK_ENV", "development")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", 1)

# Database connection
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "mysql://user:password@db:3306/objection")
SQLALCHEMY_TRACK_MODIFICATIONS = False


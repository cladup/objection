import os


# Set debug runtime environment
FLASK_ENV = os.getenv("FLASK_ENV", "development")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", 1)

# Database connection
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "mysql://user:password@db:3306/objection")
SQLALCHEMY_TRACK_MODIFICATIONS = False


import os
import pymysql
from flask import Flask, send_file
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from healthcheck import HealthCheck


# Install MySQL driver replacement
pymysql.install_as_MySQLdb()

# Import dotenv
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Init flask application
app = Flask(__name__)
app.config.from_object(os.getenv('APP_CONFIG'))

# Cross Origin
CORS(app)

# Healthcheck
health = HealthCheck(app, "/_/health")

# Configure Swagger
SWAGGER_URL = '/api/docs'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_URL + '/swagger.yaml',
    config={
        'app_name': "Objection"
    }
)

@app.route('/api/docs/swagger.yaml')
def swagger_file():
    return send_file('../docs/swagger.yaml')

# Init database with SQLAlchemy
db = SQLAlchemy(app)

# Set error handlers
@app.errorhandler(404)
def not_found(error):
    return 'Not Found', 404

# Register blueprints
from app.object.controllers import object_page
from app.admin.controllers import admin_page

app.register_blueprint(object_page)
app.register_blueprint(admin_page)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Setup database
db.create_all()


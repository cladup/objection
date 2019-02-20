import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Init flask application
app = Flask(__name__)
app.config.from_object(os.getenv('APP_CONFIG'))

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

# Setup database
db.create_all()


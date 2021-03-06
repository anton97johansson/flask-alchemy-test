from flask import Flask, jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from . import models
from .models import vegetables
# from . import views
from .views import new_routes, routes, vegetables
from app import routes

# from . import routes, models.vegetables
# from models import vegetables
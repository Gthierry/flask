import pathlib
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# charger le fichier .env
load_dotenv()

envlocal = pathlib.Path().cwd()

# je regarde si il existe
if os.path.exists(envlocal):
    load_dotenv(dotenv_path=envlocal)

app = Flask("app")
app.debug = os.environ.get("DEBUG", False)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app.controllers import *

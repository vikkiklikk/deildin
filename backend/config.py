from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" #connect to supabase later, local db for now
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #might want to enable this later but for now lets make it less complicated

db = SQLAlchemy(app) #creates a db instance that lets us access our database


from flask import Flask, Blueprint
from routes.institucion_publicas_route import instituciones_publicas
from flask_sqlalchemy import SQLAlchemy
from utils.db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3306/bd_proyecto_final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(instituciones_publicas)
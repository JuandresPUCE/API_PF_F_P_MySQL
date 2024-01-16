from flask import Flask
from routes.institucion_publicas_route import instituciones_publicas


app = Flask(__name__)

app.register_blueprint(instituciones_publicas)


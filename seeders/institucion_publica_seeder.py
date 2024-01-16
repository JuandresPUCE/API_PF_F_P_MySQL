import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3306/bd_proyecto_final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

API_URL = 'https://www.gob.ec/api/v1/instituciones'

class InstitucionPublica(db.Model):
    institucion_id = db.Column(db.Integer, primary_key=True)
    institucion = db.Column(db.String(255))
    siglas = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    url = db.Column(db.String(255))
    website = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    sector = db.Column(db.String(255))
    modificado = db.Column(db.String(255))
    publicado = db.Column(db.String(255))

def get_instituciones_publicas_from_api():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(API_URL, headers=headers, timeout=10, verify=True)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print("Error:", err)
        return None

def add_instituciones_publicas_to_db(instituciones):
    for institucion in instituciones:
        institucion_obj = InstitucionPublica.query.get(institucion['institucion_id'])
        if institucion_obj is None:
            institucion_obj = InstitucionPublica(
                institucion_id=institucion['institucion_id'],
                institucion=institucion['institucion'],
                siglas=institucion['siglas'],
                logo=institucion['logo'],
                url=institucion['url'],
                website=institucion['website'],
                tipo=institucion['tipo'],
                descripcion=institucion['descripcion'],
                sector=institucion['sector'],
                modificado=institucion['modificado'],
                publicado=institucion['publicado']
            )
            db.session.add(institucion_obj)

    db.session.commit()

def seed_instituciones_publicas():
    instituciones = get_instituciones_publicas_from_api()
    if instituciones is not None:
        add_instituciones_publicas_to_db(instituciones)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_instituciones_publicas()
from flask import Blueprint, request, jsonify
from models.institucion_publica_model import InstitucionPublica
from utils.db import db



instituciones_publicas = Blueprint('institucion_publicas', __name__)


@instituciones_publicas.route('/')
def home():
    return "listar institucion_publicas"

@instituciones_publicas.route('/instituciones_publicas/listar')
def get():
    
    return "listar institucion_publicas"

@instituciones_publicas.route('/instituciones_publicas/insertar', methods=['POST'])
def insert():
    try:
        data = request.get_json()
        new_institucion = InstitucionPublica(**data)
        db.session.add(new_institucion)
        db.session.commit()
        return jsonify(new_institucion.serialize()), 201
    except Exception as e:
        print(f"Error en la inserción: {e}")
        return jsonify({"error": "Error en la inserción"}), 500
    finally:
        db.session.close()
    
@instituciones_publicas.route('/instituciones_publicas/borrar')
def delete():
    return "borrar institucion_publicas"

@instituciones_publicas.route('/instituciones_publicas/actualizar')
def update():
    return "actualizar institucion_publicas"



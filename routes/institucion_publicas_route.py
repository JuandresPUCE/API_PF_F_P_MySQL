from flask import Blueprint, request, jsonify
from models.institucion_publica_model import InstitucionPublica
from utils.db import db



instituciones_publicas = Blueprint('institucion_publicas', __name__)


@instituciones_publicas.route('/')
def home():
    return "listar institucion_publicas"

@instituciones_publicas.route('/instituciones_publicas/listar')
def get():
    try:
        instituciones = InstitucionPublica.query.all()
        return jsonify([institucion.serialize() for institucion in instituciones]), 200
    except Exception as e:
        print(f"Error al listar las instituciones: {e}")
        return jsonify({"error": "Error al listar las instituciones"}), 500

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
    
@instituciones_publicas.route('/instituciones_publicas/borrar/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        institucion = InstitucionPublica.query.get(id)
        if institucion is None:
            return jsonify({"error": "Institución no encontrada"}), 404
        db.session.delete(institucion)
        db.session.commit()
        return jsonify({"message": "Institución borrada exitosamente"}), 200
    except Exception as e:
        print(f"Error al borrar la institución: {e}")
        return jsonify({"error": "Error al borrar la institución"}), 500

@instituciones_publicas.route('/instituciones_publicas/actualizar/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        institucion = InstitucionPublica.query.get(id)
        if institucion is None:
            return jsonify({"error": "Institución no encontrada"}), 404
        for key, value in data.items():
            setattr(institucion, key, value)
        db.session.commit()
        return jsonify(institucion.serialize()), 200
    except Exception as e:
        print(f"Error al actualizar la institución: {e}")
        return jsonify({"error": "Error al actualizar la institución"}), 500

from flask import Blueprint

instituciones_publicas = Blueprint('institucion_publicas', __name__)


@instituciones_publicas.route('/')
def home():
    return "listar institucion_publicas"

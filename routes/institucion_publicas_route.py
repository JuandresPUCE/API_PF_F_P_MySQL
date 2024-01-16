from flask import Blueprint

instituciones_publicas = Blueprint('institucion_publicas', __name__)


@instituciones_publicas.route('/')
def home():
    return "listar institucion_publicas"

@instituciones_publicas.route('/instituciones_publicas')
def get():
    return "listar institucion_publicas"

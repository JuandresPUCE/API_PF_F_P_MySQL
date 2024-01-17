#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from utils.db import db

class InstitucionPublica(db.Model):
    __tablename__ = 'instituciones_publicas'

    institucion_id = db.Column(db.Integer, primary_key=True, nullable=False)
    institucion = db.Column(db.String(255), nullable=False)
    siglas = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    tipo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    sector = db.Column(db.String(255), nullable=False)
    modificado = db.Column(db.String(255), nullable=True)
    publicado = db.Column(db.String(255), nullable=True)

    def __init__(self, **kwargs):
        super(InstitucionPublica, self).__init__(**kwargs)

    def serialize(self):
        return {
            'institucion_id': self.institucion_id,
            'institucion': self.institucion,
            'siglas': self.siglas,
            'logo': self.logo,
            'url': self.url,
            'website': self.website,
            'tipo': self.tipo,
            'descripcion': self.descripcion,
            'sector': self.sector,
            'modificado': self.modificado,
            'publicado': self.publicado
        }
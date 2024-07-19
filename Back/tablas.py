import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'ususarios'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    contraseña = db.Column(db.String(50), nullable = False)
    puntos = db.Column(db.Float)        
    email = db.Column(db.String(50))
    estados = db.relationship("EstadoSalud")

class Grupo(db.Model):
    __tablename__ = 'grupos'
    id_grupo = db.Column(db.Integer, primary_key = True)
    nombre_grupo = db.Column(db.String(50), unique = True)
    contraseña = db.Column(db.String(50), nullable = False)
    cant_integrantes = db.Column(db.Integer)

class EstadoSalud(db.Model):
    __tablename__ = 'estados_salud'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key = True)
    dia = db.Column(db.String(15), primary_key = True)
    agua = db.Column(db.Float)
    sueño = db.Column(db.Float)          
    entrenamiento =db.Column(db.Float)  

class Asignacion(db.Model):
    __tablename__ = 'asignaciones'
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key = True) #Relacionarla con usuarios y con grupo
    id_grupo = db.Column(db.Integer, db.ForeignKey('grupos.id'), primary_key = True)
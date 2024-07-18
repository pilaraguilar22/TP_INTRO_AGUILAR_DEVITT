import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'ususarios'
    id_usuario = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    contraseña = db.Column(db.String(50), nullable = False)
    puntos = db.Column(db.Integer)         #cambiar a flotante
    email = db.Column(db.String(50))

class Grupos(db.Model):
    __tablename__ = 'grupos'
    id_grupo = db.Column(db.Integer, primary_key = True)
    nombre_grupo = db.Column(db.String(50), unique = True)
    contraseña = db.Column(db.String(50), nullable = False)
    cant_integrantes = db.Column(db.Integer)

class SaludUsuarios(db.Model):
    __tablename__ = 'salud_usuarios'
    id_usuario = db.Column(db.Integer, primary_key = True) # relacionar con usuarios
    dia = db.Column(db.String(15), primary_key = True)
    agua = db.Column(db.Integer)
    sueño = db.Column(db.Integer)          # En sueño y Entrenamiento
    entrenamiento =db.Column(db.Integer)   # cambiar el tipo a flotante

class Asignaciones(db.Model):
    __tablename__ = 'asignaciones'
    id_usuario = db.Column(db.Integer, primary_key = True) #Relacionarla con usuarios y con grupo
    id_grupo = db.Column(db.Integer, primary_key = True)
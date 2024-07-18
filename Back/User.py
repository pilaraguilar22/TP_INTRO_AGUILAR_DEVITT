from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos PostgreSQL

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    fullname = db.Column(db.String(100))

    def __init__(self, username, password, fullname=""):
        self.username = username
        self.password = generate_password_hash(password)  # Hash de la contraseña al crear el usuario
        self.fullname = fullname

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)

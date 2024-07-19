from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'nombre de la base de datos'  

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100))

    def __init__(self, username, password, email=""):
        self.username = username
        self.password = generate_password_hash(password)  # Hash
        self.email = email

    @classmethod
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)

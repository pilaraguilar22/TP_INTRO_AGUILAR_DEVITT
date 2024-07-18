class Config:
    SECRET_KEY = 'Bienvenido'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:Ag@localhost/datos'  # Ajusta según tu configuración de PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    # Puedes agregar más configuraciones aquí según sea necesario
}

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import config
from User import db, User  # Importa db y User desde User.py

app = Flask(__name__, template_folder='../Front/templates')
app.static_folder = '../Front/static'
app.static_url_path = '/static'

app.config.from_object(config['development'])  # Ajusta la configuración según tus necesidades

db.init_app(app)  # Inicializa SQLAlchemy con la app Flask
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and User.check_password(user.password, password):
            login_user(user)
            return redirect(url_for('grupo'))
        else:
            flash("Usuario o contraseña incorrectos")

    return render_template('index.html')

@app.route('/grupo')
# @login_required si queres probar grupos comenta esto
def grupo():
    data = request.json
    name = data.get('username')´
    puntos = data.get('puntos')
    dia = data.get('dia')
    if request.method == 'POST':
        flash("comleta")



    return render_template('grupo/grupo.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("El nombre de usuario ya está en uso.")
        else:
            new_user = User(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("Registro exitoso. Por favor inicia sesión.")
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()




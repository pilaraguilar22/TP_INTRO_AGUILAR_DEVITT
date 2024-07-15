from flask import Flask , render_template ,request, redirect, url_for
from flask_mysqldb import MySQL
from Back import User, ModelUser  # Ajusta según la ubicación y nombres reales de tus clases
from config import config  # Ajusta según la ubicación y nombres reales de tus clases


app = Flask(__name__, template_folder='../Front/templates') 

# Configuración de la conexión a MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Cambia por tu host de MySQL
app.config['MYSQL_USER'] = 'usuario'    # Cambia por tu usuario de MySQL
app.config['MYSQL_PASSWORD'] = 'contraseña'  # Cambia por tu contraseña de MySQL
app.config['MYSQL_DB'] = 'basedatos'    # Cambia por tu nombre de base de datos en MySQL


db=MySQL(app)

app.static_folder = '../Front/static'
app.static_url_path = '/static'

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        """         print(request.form['username'])
        print(request.form['password']) """
        user= User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser()
        if logged_user!= None:
            if logged_user.password:
                return render_template('index.html') #aca pone tu ruta de cuando ves lo del grupo
            else:
                flash("contraseña invalida")
                return render_template('index.html')
        else:
            flash("Usuario no encontrdo")
            return render_template('index.html')
            
    else:
        return render_template('index.html')


if __name__== '__main__':
    app.config.from_object(config['development'])
    app.run()
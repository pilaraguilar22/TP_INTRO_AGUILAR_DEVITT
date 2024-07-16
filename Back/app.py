from flask import Flask , render_template ,request, redirect, url_for, flash
from flask_mysqldb import MySQL
 # Ajusta según la ubicación y nombres reales de tus clases
from User import User  # Ajusta según la ubicación real de User
from ModelUser import ModelUser  # Ajusta según la ubicación real de ModelUser
from config import config 
app = Flask(__name__, template_folder='../Front/templates') 


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
@app.route('/grupo')
def grupo():
    return render_template('grupo/grupo.html')
if __name__== '__main__':
    app.config.from_object(config['development'])
    app.run()
from flask import Flask, request, jsonify
from flask_cors import CORS
from tablas import db, Usuario, Grupo, EstadoSalud, Asignacion
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
CORS(app)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://fdevitt:123456@localhost:5432/baseprueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        try:
            users = Usuario.query.all()
            users_data = []
            
            for user in users:
                datos = {
                    'id': user.id,
                    'nombre': user.nombre,
                    'password': user.password,
                    'puntos': user.puntos
                }
                users_data.append(datos)  
            return jsonify({'usuarios': users_data})
        
        except Exception as error:

            print('Error', error)
            return jsonify({'message': 'Internal puto error'}), 500
    
    elif request.method == 'POST':
        try:
            data = request.get_json()
            nombre = data['nombre']
            password = data['password']
            puntos = data['puntos']
            email = data['email']

            new_user = Usuario(nombre=nombre, password=password, puntos=puntos, email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'User created successfully'}), 201
        except SQLAlchemyError as e:
            print('Database Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
        except Exception as e:
            print('General Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

    
    else:
        return "Unknown method"



@app.route('/grupos', methods=['POST'])
def post_grupo():

        try:
            data = request.get_json()
            nombre_grupo = data['nombre_grupo']
            password = data['password']
            cant_integrantes = data['cant_integrantes']



            new_group = Grupo(nombre_grupo=nombre_grupo, password=password, cant_integrantes=cant_integrantes)
            db.session.add(new_group)
            db.session.commit()
            return jsonify({'message': 'Group created successfully'}), 201
        except SQLAlchemyError as e:
            print('Database Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
        except Exception as e:
            print('General Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500



@app.route('/update_puntos/<usuario_id>', methods=['PUT'])
def update_puntos(usuario_id):
    data = request.get_json()
    nuevos_puntos = data.get("puntos")
    try:
        user = Usuario.query.filter_by(id = usuario_id).first()
        #users.puntos = nuevos_puntos

        #usuario = Usuario.query.filter_by(id=id)

        if not user:
            return jsonify({"message": "Usuario no encontrado"}), 404

        # Actualizar los puntos del usuario
        user.puntos = nuevos_puntos
        db.session.commit()

        return jsonify({"message": "Puntos cambiados con exito"})
    
    except SQLAlchemyError as e:
        print('Database Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    except Exception as e:
        print('General Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    


@app.route('/user/<username>', methods=['GET'])
def datos_usuario(username):
    
    try:
        
        datos = Usuario.query.filter_by(nombre = username).first()
        if not datos:
            return jsonify({"message": "Usuario no encontrado"}), 404

        user_data = {
            'id': datos.id,
            'nombre': datos.nombre,
            'password': datos.password,
            'puntos': datos.puntos,
            'email': datos.email
        }
        print("exito")
        return jsonify({"usuario": user_data}), 200
    
    except SQLAlchemyError as e:
        print('Database Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    except Exception as e:
        print('General Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500


@app.route('/grupos/<groupname>')
def datos_grupo(groupname):
    
    try:
        
        datos = Grupo.query.filter_by(nombre_grupo = groupname).first()
        if not datos:
            return jsonify({"message": "Grupo no encontrado"}), 404

        user_data = {
            'id_grupo': datos.id_grupo,
            'nombre_grupo ': datos.nombre_grupo ,
            'password': datos.password,
            'cant_integrantes':datos.cant_integrantes,
        }
        print("exito")
        return jsonify({"grupo": user_data}), 200
    
    except SQLAlchemyError as e:
        print('Database Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    except Exception as e:
        print('General Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500



@app.route('/asiganciones/<idUsuario>/<idGrupo>', methods=['GET', 'POST'])
def asignaciones(idUsuario,idGrupo):
    if request.method=='GET':
        try:
            datos = Asignacion.query.filter_by(id_usuario = idUsuario, id_grupo = idGrupo).first()
            if not datos:
                return jsonify({"message": "Asignacion no encontrada"}), 404
            aisgnacion_data = {
                'id_usuario': datos.id_usuario,
                'id_grupo': datos.id_grupo,
            }
            print("exito")
            return jsonify({"asignacion": aisgnacion_data}), 200
        
        except SQLAlchemyError as e:
            print('Database Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
        except Exception as e:
            print('General Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    
    elif request.method == 'POST':
        try:
            '''data = request.get_json()
            id_usuario = data['id_usuario']
            id_grupo = data['id_grupo']'''
            

            new_asignation = Asignacion(id_usuario=idUsuario, id_grupo=idGrupo)
            db.session.add(new_asignation)
            db.session.commit()
            return jsonify({'message': 'Asignation created successfully'}), 201
        except SQLAlchemyError as e:
            print('Database Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
        except Exception as e:
            print('General Error:', e)
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

    
    else:
        return "Unknown method"
    




#-----------------------------------------------------------------
@app.route('/verify_user', methods=['POST'])
def verify_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    grupo = data.get('grupo')
    password_group = data.get('password_group')

    try:
        user = Usuario.query.filter_by(nombre=username).first()
        grupo_db = Grupo.query.filter_by(nombre_grupo=grupo).first()
        if not user:
            return jsonify({"message": "Usuario no encontrado"}), 404
        
        user_data = {
            'id': user.id,
            'nombre': user.nombre,
            'password': user.password,
            'puntos': user.puntos,
            'email': user.email,
        }
        if not grupo_db:
            return jsonify({"message": "grupo no encontrado"})
        grupo_data = {
            'id_grupo': grupo_db.id_grupo,
            'nombre_grupo': grupo_db.nombre_grupo,
            'password': grupo_db.password,
            'cant_integrantes': grupo_db.cant_integrantes,
        }


        respuesta={'password':False, 'password_group':False}
        if password == user_data['password']:
            print("contraseña correcta")
            respuesta['password']=True

            if password_group == grupo_data['password']:
                respuesta['password_group']=True
            
        return jsonify({'respuesta': respuesta})
        
    
    except SQLAlchemyError as e:
        print('Database Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    except Exception as e:
        print('General Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

    
    else:
        return "Unknown method"


@app.route('/users_by_group/<grupo>', methods=['GET'])
def users_by_group(grupo):
    try:
        # Obtener el grupo especificado
        group = Grupo.query.filter_by(nombre_grupo=grupo).first()
        
        if not group:
            return jsonify({'message': 'Group not found'}), 404

        # Obtener los usuarios que pertenecen al grupo especificado a través de la tabla Asignacion
        users = db.session.query(Usuario).join(Asignacion, Usuario.id == Asignacion.id_usuario).filter(Asignacion.id_grupo == group.id_grupo).order_by(Usuario.puntos.desc()).all()
        
        users_data = []
        for user in users:
            user_data = {
                'nombre': user.nombre,
                'puntos': user.puntos,
                'email': user.email  # Incluye otros campos si los necesitas
            }
            users_data.append(user_data)
        
        return jsonify(users_data)
    except SQLAlchemyError as e:
        print('Database Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    except Exception as e:
        print('General Error:', e)
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=port)
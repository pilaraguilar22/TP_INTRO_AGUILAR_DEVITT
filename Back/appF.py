from flask import Flask, request, jsonify
#from flask_cors import CORS
from tablas import db, Usuario, Grupo, EstadoSalud, Asignacion
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
#CORS(app)
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
    


@app.route('/authors', methods=['POST'])
def add_author():
    try:
        data = request.json
        name = data.get('name')
        age = data.get('age')
        if not name or not age:
            return jsonify({'message': 'Bad request, name or age not found'}), 400
        new_author = Author(name=name, age=age)
        db.session.add(new_author)
        db.session.commit()
        return jsonify({'author': {'id': new_author.id, 'name': new_author.name, 'age': new_author.age}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        books_data = []
        for book in books:
            book_data = {
                'id': book.id,
                'isbn': book.isbn,
                'name': book.name,
                'cant_pages': book.cant_pages
            }
            books_data.append(book_data)
        return jsonify({'books': books_data})
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.json
        isbn = data.get('isbn')
        name = data.get('name')
        cant_pages = data.get('cant_pages')
        author_id = data.get('author_id')
        if not name or not cant_pages or not author_id or not isbn:
            return jsonify({'message': 'Bad request, isbn or name or cantPages or author not found'}), 400
        new_book = Book(isbn=isbn, name=name, cant_pages=cant_pages, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'book': {'id': new_book.id, 'isbn': new_book.isbn, 'name': new_book.name, 'cant_pages': new_book.cant_pages}}), 201
    except Exception as error:
        print('Error', error)
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=port)
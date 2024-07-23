

function data_recived(response) {
    return response.json();
}

function parse_registration_response(content) {
    console.log("Respuesta del servidor:", content);
    if (content.message === 'User created successfully') {
        alert('Usuario creado exitosamente. Redirigiendo al inicio de sesión.');
        window.location.href = 'http://localhost:8000/'; // Redirigir a la página de inicio de sesión
    } else {
        alert('Error al crear usuario: ' + content.message);
    }
}

function request_error(error) {
    console.error('Error en la solicitud:', error);
    alert('Ocurrió un error al intentar realizar la solicitud. Por favor, inténtelo de nuevo más tarde.');
}

function register(event){
    event.preventDefault();
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let email = document.getElementById("email").value;
    let puntos = 0

    if (!username || !password || !email) {
        alert('Por favor complete todos los campos.');
        return;
    }

    let dicc={'nombre':username, 'password':password, 'puntos':puntos, 'email':email}

    fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre: username,
            password: password,
            puntos: 0,
            email: email
        })
    })
    .then(data_recived)
    .then(parse_registration_response)
    .catch(request_error);
}

    
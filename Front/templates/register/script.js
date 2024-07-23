
function data_recived(response) {
    return response.json();
}

//maneja la respuesta de la inscripción
function parse_registration_response(content) {
    console.log("Respuesta del servidor:", content);
    if (content.message === 'Usuario creado correctamente') {
        alert('Usuario creado exitosamente. Redirigiendo al inicio de sesión.');
        window.location.href = 'http://localhost:8000/'; // Redirigir a la página de inicio de sesión
    } else {
        alert('Error al crear usuario: ' + content.message);
    }
}

// maneja errores de la solicitud
function request_error(error) {
    console.error('Error en la solicitud:', error);
    alert('Ocurrió un error al intentar realizar la solicitud. Por favor, inténtelo de nuevo más tarde.');
}

//  registra un nuevo usuario
function register(event) {
    event.preventDefault(); // Evita el envío del formulario

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let email = document.getElementById("email").value;
    let puntos = 0;

    if (!username || !password || !email) {
        alert('Por favor complete todos los campos.');
        return;
    }

    let dicc = {
        nombre: username,
        password: password,
        puntos: puntos,
        email: email
    };

    fetch(`http://localhost:5000/user/${username}`, {   //api linea 17
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dicc)
    })
    .then(data_recived)
    .then(parse_registration_response)
    .catch(request_error);
}

// Añadir el event listener al formulario
document.getElementById('registroForm').addEventListener('submit', register);

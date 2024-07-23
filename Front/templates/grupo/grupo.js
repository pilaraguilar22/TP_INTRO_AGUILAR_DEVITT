//--------------funciones de los contadores de salud---------//

function sumar_entrenamiento() {
    let i = parseInt(document.getElementById("hs_entrenamiento").innerText);
    i++;
    document.getElementById("hs_entrenamiento").innerText = i;
}

function restar_entrenamiento() {
    let i = parseInt(document.getElementById("hs_entrenamiento").innerText);
    if (i > 0) {
        i--;
        document.getElementById("hs_entrenamiento").innerText = i;
    }
}

function sumar_sueño() {
    let i = parseInt(document.getElementById("hs_sueño").innerText);
    i++;
    document.getElementById("hs_sueño").innerText = i;
}

function restar_sueño() {
    let i = parseInt(document.getElementById("hs_sueño").innerText);
    if (i > 0) {
        i--;
        document.getElementById("hs_sueño").innerText = i;
    }
}

function sumar_agua() {
    let i = parseInt(document.getElementById("vasos_agua").innerText);
    i++;
    document.getElementById("vasos_agua").innerText = i;
}

function restar_agua() {
    let i = parseInt(document.getElementById("vasos_agua").innerText);
    if (i > 0) {
        i--;
        document.getElementById("vasos_agua").innerText = i;
    }
}


//-------------------------Actualiza los puntos------------------------//
function asignar_puntos() {
    let horas_de_sueno = parseFloat(document.getElementById("hs_sueño").value);
    let vasos_de_agua = parseFloat(document.getElementById("vasos_agua").value);
    let horas_de_entrenamiento = parseFloat(document.getElementById("hs_entrenamiento").value);

    const user = urlParams.get('usuario');
    let nuevos_puntos = 15;

    if (9 > horas_de_sueno && horas_de_sueno > 6) {
        nuevos_puntos += (horas_de_sueno * 10);
    }
    if (20 > vasos_de_agua && vasos_de_agua > 5) {
        nuevos_puntos += (vasos_de_agua * 10);
    }
    if (5 > horas_de_entrenamiento) {
        nuevos_puntos += (horas_de_entrenamiento * 50);
    }

    fetch(`http://localhost:5000/update_puntos/${user}`, {  // api linea 117
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ puntos: nuevos_puntos })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Respuesta del servidor:", data);
        if (data.message === "Puntos cambiados con exito") {
            alert('Puntos actualizados correctamente');
        } else {
            alert('Error al actualizar puntos: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
        alert('Ocurrió un error al intentar actualizar los puntos. Por favor, inténtelo de nuevo más tarde.');
    });
}

//-----------------Poniendo el nomre del Grupo---------------------//
const urlParams = new URLSearchParams(window.location.search); //saco los parametros de la url
console.log('parametros:', new URLSearchParams(window.location.search))
const grupo = urlParams.get('grupo'); //guardo el grupo

let nombre_grupo = document.createElement("h1"); //creo el H1
nombre_grupo.textContent = grupo; 
nombre_grupo.classList.add("rounded-5");
document.getElementById("grupo").appendChild(nombre_grupo); //Al contenedor con id=grupo le inserto el H1

//------------------- Cargando la tabla -------------------------//

function populateTable(users) {
    const tablaBody = document.getElementById("tabla-body");
    users.forEach((user, index) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <th scope="row">${index + 1}</th>
            <td>${user.nombre}</td>
            <td>${user.puntos}</td>
        `;
        tablaBody.appendChild(fila);
    });
}

// Realizar la solicitud fetch para obtener los usuarios ordenados por puntos
fetch(`http://localhost:5000/users_by_group/${grupo}`)  //api linea 302
    .then(response => response.json())
    .then(data => {
        console.log('Usuarios:', data);
        populateTable(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });



//llama a la funcionde eliminar usuario al apretar el boton
document.addEventListener('DOMContentLoaded', (event) => {
    const deleteButton = document.getElementById('delete-button');
    deleteButton.addEventListener('click', eliminarUsuario);
});
function eliminarUsuario() {
    const usuario = encodeURIComponent(urlParams.get('usuario'));

    fetch(`http://localhost:5000/user/${usuario}`, {   //api linea 17
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        console.log("Respuesta del servidor:", data);
        if (data.message === "Usuario eliminado correctamente") {
            alert('Usuario eliminado correctamente');
            window.location.href = 'http://localhost:8000/'
        } else {
            alert('Error al eliminar usuario: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
        alert('Ocurrió un error al intentar eliminar el usuario. Por favor, inténtelo de nuevo más tarde.');
    });
}

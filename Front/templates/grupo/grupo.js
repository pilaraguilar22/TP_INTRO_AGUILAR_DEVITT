
function sumar_entrenamiento() {
    let i = parseInt(document.getElementById("contador1").innerText);
    i++;
    document.getElementById("contador1").innerText = i;
}

function restar_entrenamiento() {
    let i = parseInt(document.getElementById("contador1").innerText);
    if (i > 0) {
        i--;
        document.getElementById("contador1").innerText = i;
    }
}

function sumar_sueño() {
    let i = parseInt(document.getElementById("contador2").innerText);
    i++;
    document.getElementById("contador2").innerText = i;
}

function restar_sueño() {
    let i = parseInt(document.getElementById("contador2").innerText);
    if (i > 0) {
        i--;
        document.getElementById("contador2").innerText = i;
    }
}

function sumar_agua() {
    let i = parseInt(document.getElementById("contador3").innerText);
    i++;
    document.getElementById("contador3").innerText = i;
}

function restar_agua() {
    let i = parseInt(document.getElementById("contador3").innerText);
    if (i > 0) {
        i--;
        document.getElementById("contador3").innerText = i;
    }
}


function asignar_puntos(horas_de_dueño,vasos_de_agua,horas_de_enrenamiento) {
    let dia= getElementById("dia").value;
    let id= getElementById("id").value;

    let puntos = 0;
    if (9 > horas_de_dueño && horas_de_dueño > 6) {
        puntos+=(horas_de_dueño*10);
    }
    if (20 > vasos_de_agua && vasos_de_agua > 5) {
        puntos+=(vasos_de_agua*10);
    }
    if (5 > horas_de_enrenamiento ) {
        puntos+=(horas_de_enrenamiento*50);
    }

    const data={'puntos':puntos};
    const response=fetch("/grupo",{method: 'PUT', headers:{
        'Content-Type':'/json'
    },
    body:JSON.stringify(data)

})

    return puntos;
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
fetch(`http://localhost:5000/users_by_group/${grupo}`)
    .then(response => response.json())
    .then(data => {
        console.log('Usuarios:', data);
        populateTable(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });


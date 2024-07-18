// Funciones para manipular los contadores de actividades
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

// Genera dinámicamente el nombre del grupo
const nombre = "Doble 9"; // Recibido del servidor o base de datos
let nombre_grupo = document.createElement("h1");
nombre_grupo.textContent = nombre;
nombre_grupo.classList.add("rounded-5");
document.getElementById("grupo").appendChild(nombre_grupo);

// Datos simulados para la tabla de puntos de salud
const tabla_puntos = {
    "Francisco Devitt": 15,
    "Pilar Aguilar": 12,
    "Manu Camejo": 9,
    "Manu Bilbao": 7
};

// Genera dinámicamente las filas de la tabla
const tablaBody = document.getElementById("tabla-body");
Object.keys(tabla_puntos).forEach((nombre, index) => {
    const puntos = tabla_puntos[nombre];
    const fila = document.createElement("tr");
    fila.innerHTML = `
        <th scope="row">${index + 1}</th>
        <td>${nombre}</td>
        <td>${puntos}</td>
    `;
    tablaBody.appendChild(fila);
});

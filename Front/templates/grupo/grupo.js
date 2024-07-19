
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




const nombre = "Doble 9"; // Recibido  base de datos
let nombre_grupo = document.createElement("h1");
nombre_grupo.textContent = nombre;
nombre_grupo.classList.add("rounded-5");
document.getElementById("grupo").appendChild(nombre_grupo);

// Datos simulados
const tabla_puntos = {
    "Francisco Devitt": 15,
    "Pilar Aguilar": 12,
    "Manu Camejo": 9,
    "Manu Bilbao": 7
};

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

//Genera el H1 con el nombre del grupo
const nombre="Doble 9" //recibo el nombre del grupo de la base de datos
let nombre_grupo=document.createElement("h1")

nombre_grupo.append(nombre)
nombre_grupo.classList.add("rounded-5")
document.getElementById("grupo").append(nombre_grupo)



//para crear la tabla:

//simulo tener personas

let tabla_puntos = {"Francisco Devitt":15, "Pilar Aguilar":12, "Manu Camejo":9, "Manu Bilbao":7}

let usuarios = Object.keys(tabla_puntos)

//REVISAR ESTOOOOO!!!!

for (let i = 0; i < usuarios.length; i++) {
    const puntos = tabla_puntos[usuarios[i]];

    const fila = document.createElement("tr")
    const col_puestos = document.createElement("th")
    const col_nombres = document.createElement("td")
    const col_puntos = document.createElement("td")

    col_puestos.append(1)
    col_nombres.innerText(usuarios[i])
    col_puntos.innerText(puntos)

    fila.append(col_puestos)
    fila.append(col_nombres)
    fila.append(col_puntos)

    document.getElementById("tabla-body").append(fila)
    
}
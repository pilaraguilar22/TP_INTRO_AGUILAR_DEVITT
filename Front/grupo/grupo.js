//let contador= document.getElementById("contador1").innerText;
//console.log(contador);




//contadores de la actividad entrenamiento
function sumar_entrenamiento(){
    let i= parseInt(contador1.innerText);
    i++;

    contador1.innerText =i;

}

function restar_entrenamiento(){
    let i= parseInt(contador1.innerText);
    
    if (i>0){
        
        i--;
    
        contador1.innerText =i;
    };

}


//contadores de la actividad horas de sueño
function sumar_sueño(){
    let i= parseInt(contador2.innerText);
    i++;

    contador2.innerText =i;

}

function restar_sueño(){
    let i= parseInt(contador2.innerText);
    
    if (i>0){
        
        i--;
    
        contador2.innerText =i;
    };

}

//contadores de la actividad vasos de agua
function sumar_agua(){
    let i= parseInt(contador3.innerText);
    i++;

    contador3.innerText =i;

}

function restar_agua(){
    let i= parseInt(contador3.innerText);
    
    if (i>0){
        
        i--;
    
        contador3.innerText =i;
    };

}

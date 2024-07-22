document.addEventListener("DOMContentLoaded", function() {
    const btnSignIn = document.getElementById("sign-in");
    const btnSignUp = document.getElementById("sign-up");

    btnSignIn.addEventListener("click", function() {
        window.location.href = "/login"; 
    });

    btnSignUp.addEventListener("click", function() {
        window.location.href = "/register"; 
    });
});

//------------------ FUNCIONES PARA LOGIN --------------------//

function data_recived(response) {
    return response.json();
}

function parse_data_usuario(content) {
    console.log("Contenido:", content);
    let grupo= document.getElementById("grupo").value;
    if (content.respuesta.password && content.respuesta.password_group){
        window.location.href = `http://localhost:8000/grupo?grupo=${grupo}`
    }else{
        alert('No se encontraron credenciales válidas para el usuario o el grupo.');
    }
    
}

function request_error(error) {
    console.log(error);
}

function login(event){
    event.preventDefault();
    let username= document.getElementById("username").value;
    let password= document.getElementById("password").value;
    let grupo= document.getElementById("grupo").value;
    let password_group= document.getElementById("password_group").value;

    fetch('http://localhost:5000/verify_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password,
            grupo: grupo,
            password_group: password_group
        })
    })
    .then(data_recived)
    .then(parse_data_usuario)
    .catch(request_error);

}
    
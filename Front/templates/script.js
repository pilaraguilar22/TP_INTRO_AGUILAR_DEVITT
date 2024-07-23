
//------------------ FUNCIONES PARA LOGIN --------------------//

function data_recived(response) {
    return response.json();
}

function parse_data_usuario(content) {
    console.log("Contenido:", content);
    let grupo= document.getElementById("grupo").value;
    let user= document.getElementById("username").value;    

    if (content.respuesta.password && content.respuesta.password_group){
        window.location.href = `http://localhost:8000/grupo?grupo=${grupo}&usuario=${user}`
    }else{
        alert('Las credencialies de ingreso no son validas');
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
    
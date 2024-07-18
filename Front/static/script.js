document.addEventListener("DOMContentLoaded", function() {
    const btnSignIn = document.getElementById("sign-in");
    const btnSignUp = document.getElementById("sign-up");

    btnSignIn.addEventListener("click", function() {
        window.location.href = "/login"; // Redirige a la página de inicio de sesión
    });

    btnSignUp.addEventListener("click", function() {
        window.location.href = "/register"; // Redirige a la página de registro
    });
});

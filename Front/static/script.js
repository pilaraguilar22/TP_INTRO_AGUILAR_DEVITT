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

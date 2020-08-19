var name=localStorage.getItem("name");
var email=localStorage.getItem("email");

document.getElementById("message").innerHTML = name;
document.getElementById("email").innerHTML = email;

document.getElementById("cred1").value = email;
document.getElementById("cred2").value = name;
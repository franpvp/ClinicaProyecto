/* Validaciones de los campos en Registro.*/

/* Input nombre:*/

const divForm1 = document.querySelector("#formFloating1");
const nombres = document.querySelector("#nombres");
const errorNombre = document.querySelector('#nombreInvalido');

const valNombres =()=>{
    let texto = document.getElementById("nombres").value;
    let hayNumero = /[0-9]+/.test(texto);

    if(texto === "" || texto == null) {
        errorNombre.innerHTML = "Por favor, ingrese su primer y segundo nombre ";
        divForm1.classList.add("is-invalid");
        nombres.classList.add("is-invalid");
    } 
    else if((texto !== "" || texto !== null) && hayNumero) {
        errorNombre.innerHTML = "Este campo no puede tener números";
        divForm1.classList.add("is-invalid");
        nombres.classList.add("is-invalid");
    } 
    else {
        divForm1.classList.remove("is-invalid");
        nombres.classList.remove("is-invalid");
        nombres.classList.add("is-valid");
    }
}

/* Input Apellidos*/

const divForm2 = document.querySelector("#formFloating2");
const apellidos = document.querySelector("#apellidos");
const errorApellido = document.querySelector("#apellidoInvalido");

const valApellidos = () => {
    let texto = document.getElementById("apellidos").value;
    let hayNumero = /[0-9]+/.test(texto);

    if(texto === "" || texto === null){
        errorApellido.innerHTML = "Por favor, ingrese su primer y segundo apellido";
        apellidos.classList.add("is-invalid");
        divForm2.classList.add("is-invalid");
    }
    else if((texto !== "" || texto !== null) && hayNumero){
        errorApellido.innerHTML = "Este campo no debe contener números";
        apellidos.classList.add("is-invalid");
        divForm2.classList.add("is-invalid");
    }
    else {
        divForm2.classList.remove("is-invalid");
        apellidos.classList.remove("is-invalid");
        apellidos.classList.add("is-valid");
    }
}

/* Input correo */

const divForm3 = document.querySelector("#formFloating3");
const email = document.querySelector("#email");
const errorEmail = document.querySelector("#emailInvalido");

const valEmail = () => {
    let texto = document.getElementById("email").value;
    let emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]+$/;

    if(texto === "" || texto === null){
        errorEmail.innerHTML = "Por favor ingrese un correo electrónico";
        email.classList.add("is-invalid");
        divForm3.classList.add("is-invalid");
    }
    else if(emailRegex.test(texto)){
        divForm3.classList.remove("is-invalid");
        email.classList.remove("is-invalid");
        email.classList.add("is-valid");
    }
    else {
        console.log("Campo Inválido");
        errorEmail.innerHTML = "El correo debe tener el formato 'nombre@gmail.com'";
        email.classList.add("is-invalid");
        divForm3.classList.add("is-invalid");
    }
}

/* Input Usuario */

const divForm4 = document.querySelector("#formFloating4");
const usuario = document.querySelector("#nombreUsuario");
const errorUsuario = document.querySelector("#usuarioInvalido");

const valUsername = () => {
    let textoUser = document.getElementById("nombreUsuario").value;

    if(textoUser === "" || textoUser === null){
        errorUsuario.innerHTML = "Debe llenar este campo";
        divForm4.classList.add("is-invalid");
        usuario.classList.add("is-invalid");
    }
    else {
        divForm4.classList.remove("is-invalid");
        usuario.classList.remove("is-invalid");
        usuario.classList.add("is-valid");
    }
}

/* Validaciones de eyes icons */

const visibilityBtn1 = document.getElementById("visibilityEye1");
visibilityBtn1.addEventListener("click", toggleVisibility1);

function toggleVisibility1 () {
    let passwordInput = document.getElementById("contraseña1");
    let icon = document.getElementById("icon1");
    if(passwordInput.type === "password"){
        passwordInput.type = "text";
        icon.innerText = "visibility";
    } else {
        passwordInput.type = "password";
        icon.innerText = "visibility_off";
    }
}

const visibilityBtn2 = document.getElementById("visibilityEye2");
visibilityBtn2.addEventListener("click", toggleVisibility2);

function toggleVisibility2 () {
    let passwordInput = document.getElementById("contraseña2");
    let icon = document.getElementById("icon2");
    if(passwordInput.type === "password"){
        passwordInput.type = "text";
        icon.innerText = "visibility";
    } else {
        passwordInput.type = "password";
        icon.innerText = "visibility_off";
    }
}

/* Input Contraseña1 */

/* 
En cuanto a las contraseñas, se deberán proporcionar al menos 4 validaciones de 
seguridad de estas para protección tales como longitud mínima, uso de caracteres 
especiales, uso de números y letras, longitud máxima o alguna otra que considere esencial.
*/

const divForm5 = document.querySelector("#formFloating5");
const passWord1 = document.querySelector("#contraseña1");
const errorPass1 = document.querySelector("#passInvalid1");

const valPass1 = () => {
    let textPass1 = document.getElementById("contraseña1").value;
    let passRegex = /(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9].*[0-9])(?=.*[^a-zA-Z0-9]).{5,}/;

    if(textPass1 === "" || textPass1 === null){
        errorPass1.innerHTML = "Este campo tiene que ser llenado";
        divForm5.classList.add("is-invalid");
        passWord1.classList.add("is-invalid");
    }
    else if(passRegex.test(textPass1)){
        console.log("Contraeña correcta");
        divForm5.classList.remove("is-invalid");
        passWord1.classList.remove("is-invalid");
        passWord1.classList.add("is-valid");
    }
    else {
        console.log("Contraseña incorrecta");
        errorPass1.innerHTML = "Debe contener al menos 1 letra mayúscula, 1 letra minúscula, 2 dígitos y 1 caracter especial. Además, el mínimo de caracteres permitidos es de 5.";
        divForm5.classList.add("is-invalid");
        passWord1.classList.add("is-invalid");
    }
}

/*  Input Contraseña 2 */

const divForm6 = document.querySelector("#formFloating6");
const passWord2 = document.querySelector("#contraseña2");
const errorPass2 = document.querySelector("#passInvalid2");

const valPass2 = () => {
    let textPass2 = document.getElementById("contraseña2").value;

    if(textPass2 === "" || textPass2 === null){
        errorPass2.innerHTML = "Este campo debe ser llenado";
        divForm6.classList.add("is-invalid");
        passWord2.classList.add("is-invalid");
    }
    else if(passWord1.value === passWord2.value){
        console.log("Las contraseñas son iguales");
        divForm6.classList.remove("is-invalid");
        passWord2.classList.remove("is-invalid");
        passWord2.classList.add("is-valid");
    }
    else {
        console.log("Las contraseñas no son iguales");
        errorPass2.innerHTML = "Las contraseñas no son iguales";
        divForm6.classList.add("is-invalid");
        passWord2.classList.add("is-invalid");
    }
}

/* Input de Domicilio*/

const divForm7 = document.querySelector("#formFloating7");
const direccion = document.querySelector("#direccion");
const errorDireccion = document.querySelector("#errorDireccion");

const valDireccion = () => {
    let textoDireccion = document.getElementById("direccion").value;
    let dirRegex = /^[a-zA-ZÀ-ÿ]+\s[0-9]{1,4}|\s[a-zAÀ-ÿ-Z0-9]+|\s[a-zAÀ-ÿ-Z0-9]+$/;

    if(textoDireccion === "" || textoDireccion === null){
        errorDireccion.innerHTML = "La direccion debe ser llenada"
        divForm7.classList.add("is-invalid");
        direccion.classList.add("is-invalid");
    } 
    else if(dirRegex.test(textoDireccion)){
        console.log("Es valida la contraseña");
        divForm7.classList.remove("is-invalid");
        direccion.classList.remove("is-invalid");
        direccion.classList.add("is-valid");
    }
    else {
        console.log("Debe contener numeros y letras");
        errorDireccion.innerHTML = "La direccion tiene que tener un formato mínimo: 'Calle 0000'";
        divForm7.classList.add("is-invalid");
        direccion.classList.add("is-invalid");
    }
}

/* Input Fecha de Nacimiento */


const divForm8 = document.querySelector("#formFloating8");
const fecha = document.querySelector("#fechaNacimiento");
const errorFecha = document.querySelector("#fechaInvalida");

const valFecha = () => {
    let textoFecha = document.getElementById("fechaNacimiento").value;

    if(textoFecha === "" || textoFecha === null){
        errorFecha.innerHTML = "Ingrese una fecha de nacimiento"
        divForm8.classList.add("is-invalid");
        fecha.classList.add("is-invalid");
    }
    else {
        divForm8.classList.remove("is-invalid");
        fecha.classList.remove("is-invalid");
        fecha.classList.add("is-valid");
    }
}

/* Input de Limpiar Formulario */

const formulario = document.querySelector("#formulario");

const limpiarFormulario = () => {
    formulario.reset();
}

/* Input de Enviar Formulario */

let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

let nombre = id("nombres"),
    apellido = id("apellidos"),
    correo = id("email"),
    user = id("nombreUsuario"),
    password1 = id("constraseña1"),
    password2 = id("contraseña2"),
    adress = id("direccion"),
    date = id("fechaNacimiento"),
    boton = id("boton"),
    form = id("formulario"),
    errorMsg = classes("error");

form.addEventListener("click", (e) => {
    e.preventDefault();
    
    control(nombre, 0, " ");
    control(apellido, 1, " ");
    control(correo, 2, " ");
    control(user, 3, " ");
    control(passWord1, 4, " ");
    control(passWord2, 5, " ");
    control(adress, 6, " ");
    control(date, 7, " ");
    
});

const errorBoton = document.querySelector("#boton");

let control = (id, serie, msg) => {
    if(id.value.trim() === ""){
        errorMsg[serie].innerHTML = msg;
        errorMsg[8].innerHTML = "Todos los campos tienen que ser llenados";
    } 
    else {
        errorMsg[serie].innerHTML = "";
        errorMsg[8].innerHTML = " ";
    }
}

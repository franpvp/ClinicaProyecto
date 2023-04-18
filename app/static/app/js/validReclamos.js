/* Validaciones de los campos en Reclamos*/

/* Input Nombre */

const div1 = document.querySelector("#div1");
const nombre1 = document.querySelector("#nombres");
const error1 = document.querySelector("#nombreInvalido");

let valNombre = () => {
    let texto = document.getElementById("nombres").value;
    let hayNumero = /[0-9]+/.test(texto);

    if(texto === "" || texto == null) {
        error1.innerHTML = "Por favor, ingrese su primer y segundo nombre";
        div1.classList.add("is-invalid");
        nombre1.classList.add("is-invalid");
    } 
    else if((texto !== "" || texto !== null) && hayNumero) {
        error1.innerHTML = "Este campo no puede tener números";
        div1.classList.add("is-invalid");
        nombre1.classList.add("is-invalid");
    } 
    else {
        div1.classList.remove("is-invalid");
        nombre1.classList.remove("is-invalid");
        nombre1.classList.add("is-valid");
    }
}

const div2 = document.querySelector("#div2");
const apellido2 = document.querySelector("#apellidos");
const error2 = document.querySelector("#apellidoInv");

let valApellido = () => {
    let texto = document.getElementById("apellidos").value;
    let hayNumero = /[0-9]+/.test(texto);

    if(texto === "" || texto === null){
        error2.innerHTML = "Por favor, ingrese su primer y segundo apellido";
        apellido2.classList.add("is-invalid");
        div2.classList.add("is-invalid");
    }
    else if((texto !== "" || texto !== null) && hayNumero){
        error2.innerHTML = "Este campo no debe contener números";
        apellido2.classList.add("is-invalid");
        div2.classList.add("is-invalid");
    }
    else {
        div2.classList.remove("is-invalid");
        apellido2.classList.remove("is-invalid");
        apellido2.classList.add("is-valid");
    }
}

const div3 = document.querySelector("#div3");
const textoRut = document.querySelector("#rut");
const error3 = document.querySelector("#rutInv");

let valRut = () => {
    let texto = document.getElementById("rut").value;
    let rutRegex = /^([1-9]|[1-9]\d|[1-9]\d{2})(\.\d{3})*\-(\d|k|K)$/;

    if(texto === "" || texto === null){
        console.log("textoRut invalido");
        error3.innerHTML = "Por favor, llene este campo del Rut";
        textoRut.classList.add("is-invalid");
        div3.classList.add("is-invalid");
    }
    else if(rutRegex.test(texto)){
        div3.classList.remove("is-invalid");
        textoRut.classList.remove("is-invalid");
        textoRut.classList.add("is-valid");
    }
    else {
        console.log("Debe contener numeros y letras");
        error3.innerHTML = "El Rut debe tener este formato: '00.000.000-0'";
        div3.classList.add("is-invalid");
        textoRut.classList.add("is-invalid");
    }
}

const div4 = document.querySelector("#div4");
const celular = document.querySelector("#celular");
const error4 = document.querySelector("#celularInv");

let valCelu = () => {
    let texto = document.getElementById("celular").value;
    let celularRegex = /^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$/;

    if(texto === "" || texto === null){
        console.log("celular invalido");
        error4.innerHTML = "Por favor, llene este campo con el celular";
        celular.classList.add("is-invalid");
        div4.classList.add("is-invalid");
    }
    else if(celularRegex.test(texto)){
        div4.classList.remove("is-invalid");
        celular.classList.remove("is-invalid");
        celular.classList.add("is-valid");
    }
    else {
        console.log("Debe contener numeros y letras");
        error4.innerHTML = "El celular debe tener este formato: '+56 9 11112222'";
        div4.classList.add("is-invalid");
        celular.classList.add("is-invalid");
    }
}

const div5 = document.querySelector("#div5");
const direccion = document.querySelector("#direccion");
const error5 = document.querySelector("#direccionInv");

const valDireccion = () => {
    let texto = document.getElementById("direccion").value;
    let dirRegex = /^[a-zA-ZÀ-ÿ]+\s[0-9]{1,4}|\s[a-zAÀ-ÿ-Z0-9]+|\s[a-zAÀ-ÿ-Z0-9]+$/;

    if(texto === "" || texto === null){
        console.log("Direccion");
        error5.innerHTML = "La direccion debe ser llenada"
        div5.classList.add("is-invalid");
        direccion.classList.add("is-invalid");
    } 
    else if(dirRegex.test(texto)){
        console.log("Es valida la contraseña");
        div5.classList.remove("is-invalid");
        direccion.classList.remove("is-invalid");
        direccion.classList.add("is-valid");
    }
    else {
        console.log("Debe contener numeros y letras");
        error5.innerHTML = "La direccion tiene que tener un formato mínimo: 'Calle 0000'";
        div5.classList.add("is-invalid");
        direccion.classList.add("is-invalid");
    }
}

/* Validaciones de los campos con el bottom Enviar */

let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

let nombre = id("nombres"),
    apellido = id("apellidos"),
    rut = id("rut"),
    celu = id("celular"),
    adress = id("direccion"),
    boton = id("boton"),
    form = id("formulario"),
    errorMsg = classes("error");

form.addEventListener("click", (e) => {
    e.preventDefault();
    
    control(nombre, 0, " ");
    control(apellido, 1, " ");
    control(adress, 2, " ");
    control(date, 3, " ");
    
});

const errorBoton = document.querySelector("#boton");

let control = (id, serie, msg) => {
    if(id.value.trim() === ""){
        errorMsg[serie].innerHTML = msg;
        errorMsg[5].innerHTML = "Los primeros 5 campos tienen que ser llenados";
    } 
    else {
        errorMsg[serie].innerHTML = "";
        errorMsg[5].innerHTML = " ";
    }
}

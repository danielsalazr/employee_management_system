const SearchEmployeeToupdate = document.querySelector('#SearchEmployeeToupdate');
const removeSearchEmployeeToupdate = document.querySelector('#removeSearchEmployeeToupdate')
const numero_documento = document.querySelector('#numero_documento');
const nombre = document.querySelector("#nombre");
const apellido = document.querySelector("#apellido");
const tipo_documento = document.querySelector("#tipo_documento");
const telefono = document.querySelector("#telefono");
const sangre = document.querySelector("#sangre");
const correo = document.querySelector("#correo");
const submitEmployeeUpdateInfo = document.querySelector('#submitEmployeeUpdateInfo');

function setReadonlyInput(condition){
    nombre.readOnly = condition
    apellido.readOnly = condition
    tipo_documento.readOnly = condition
    telefono.readOnly = condition
    sangre.readOnly = condition
    correo.readOnly = condition
    submitEmployeeUpdateInfo.disabled = condition;
}

function eraseInputs(){
  nombre.value = '';
  apellido.value = '';
  tipo_documento.value = '';
  telefono.value = '';
  sangre.value = '';
  correo.value = '';
}

const searchEmployee = async () => {

  if (numero_documento.value === ''){
      await swalErr('Debe ingresar un numero de documento para obtener informacion del colaborador');
      // await setTimeout(numero_documento.focus(),3000)
      return  setTimeout(numero_documento.focus(),2000)
  }

  const url = `empleados/?id=${numero_documento.value}`;
  const req = await callApi(url);

  if (req.res.status !== 200){
      // numero_documento.value = '';
      nombre.value = '';
      apellido.value = '';
      tipo_documento.value = '';
      telefono.value = '';
      sangre.value = '';
      correo.value = '';

      setReadonlyInput(true);
      await swalErr('No se logro obtener un empleado con este dato');
      // setTimeout(numero_documento.focus(),2000)
      return 
  }
  const data = req.data[0]

  console.log(data)

  setReadonlyInput(false);
  numero_documento.readOnly= true;
  numero_documento.value = data.numero_documento;
  nombre.value = data.nombre;
  apellido.value = data.apellido;
  tipo_documento.value = data.tipoDocumento;
  telefono.value = data.telefono;
  sangre.value = data.tipoSangre;
  correo.value = data.correo;

  removeSearchEmployeeToupdate.disabled = false;
  SearchEmployeeToupdate.disabled = true;
}

setReadonlyInput(true);
removeSearchEmployeeToupdate.disabled = true;


//This function only receives true or false value, and i use to block default inputs


numero_documento.focus()


// numero_documento.addEventListener('focus',() => {
removeSearchEmployeeToupdate.addEventListener('click',() => {
  removeSearchEmployeeToupdate.disabled = true;
  SearchEmployeeToupdate.disabled = false;
  numero_documento.readOnly= false;
  eraseInputs();
  setReadonlyInput(true);
})


numero_documento.addEventListener("keydown", (event) => {
    
    if (event.keyCode === 13) {
      event.preventDefault();
      
      return searchEmployee();
    }
  
});
SearchEmployeeToupdate.addEventListener('click',() => searchEmployee());













function crearEmpleado() {
    const url = "/creacion/";
    let data = {
      numero_documento: 0,
      nombre: "",
      apellido: "",
      tipo_documento: "",
      correo: "",
      telefono: 0,
      tipo_sangre: "",
      foto:"",
    };

    data.numero_documento =  document.getElementById("numero_documento").valueAsNumber;
    data.nombre = document.getElementById("nombre").value;
    data.apellido = document.getElementById("apellido").value;
    data.tipo_documento = document.getElementById("tipo_documento").value;
    data.correo = document.getElementById("correo").value;
    data.telefono = document.getElementById("telefono").valueAsNumber;
    data.tipo_sangre = document.getElementById("sangre").value;
    data.foto = document.getElementById("foto");
    //data.image = document.getElementById("image").value;


    console.log(data.nombre);
    console.log(data.apellido);
    console.log(typeof(data.numero_documento));
    console.log(typeof(data.telefono));

    

    //var myInit = { method: 'GET',
    //       headers: myHeaders,
    //       mode: 'cors',
    //       cache: 'default' };

    const formData = new FormData();
    //console.log(name);
    formData.append('numero_documento', data.numero_documento);
    formData.append('nombre', data.nombre);
    formData.append('apellido', data.apellido);
    formData.append('tipo_documento', data.tipo_documento);
    formData.append('correo', data.correo);
    formData.append('telefono',data.telefono );
    formData.append('tipo_sangre', data.tipo_sangre);
    formData.append('foto', data.foto.files[0]);
    //formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');
    console.log(data);


    axios.defaults.headers = {
      "Content-Type": "application/json",
      // 'X-CSRFToken': 'csrftoken',
      'content-type': 'multipart/form-data',
    }
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    axios({
        method: 'put',
        url: url,
        data: formData,
        // {
        //   name:data.name,
        //   sku:data.sku,
        //   }
      })
      .then(res => {
        console.log(res.data);
      })
  }
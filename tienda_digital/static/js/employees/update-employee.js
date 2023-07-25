const SearchEmployeeToupdate = document.querySelector('#SearchEmployeeToupdate');
const numero_documento = document.querySelector('#numero_documento');
const nombre = document.querySelector("#nombre");
const apellido = document.querySelector("#apellido");
const tipo_documento = document.querySelector("#tipo_documento");
const telefono = document.querySelector("#telefono");
const sangre = document.querySelector("#sangre");
const correo = document.querySelector("#correo");

function setReadonlyInput(condition){
    nombre.readOnly = condition
    apellido.readOnly = condition
    tipo_documento.readOnly = condition
    telefono.readOnly = condition
    sangre.readOnly = condition
    correo.readOnly = condition
}

function eraseInputs(){
  nombre.value = '';
  apellido.value = '';
  tipo_documento.value = '';
  telefono.value = '';
  sangre.value = '';
  correo.value = '';
}

setReadonlyInput(true);


//This function only receives true or false value, and i use to block default inputs


numero_documento.focus()


numero_documento.addEventListener('focus',() => {
  eraseInputs();
  setReadonlyInput(true);
})


SearchEmployeeToupdate.addEventListener('click', async () => {

    if (numero_documento.value == ''){
        swalErr('Debe ingresar un numero de documento para obtener informacion del colaborador')
        return
    }
    
    const url = `empleados/?numero_documento=${numero_documento.value}`;
    const req = await callApi(url);

    if (req.res.status !== 200){

        numero_documento.value = '';
        nombre.value = '';
        apellido.value = '';
        tipo_documento.value = '';
        telefono.value = '';
        sangre.value = '';
        correo.value = '';

        setReadonlyInput(true);

    
        await swalErr('No se logro obtener un empleado con este dato');
        return
    }

    const data = req.data

    setReadonlyInput(false);

    numero_documento.value = data.numero_documento;
    nombre.value = data.nombre;
    apellido.value = data.apellido;
    tipo_documento.value = data.tipo_documento;
    telefono.value = data.telefono;
    sangre.value = data.tipo_sangre;
    correo.value = data.correo;
    
});













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
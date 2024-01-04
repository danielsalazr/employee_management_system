const studiesForm = document.querySelector('#experienceForm')

studiesForm.addEventListener('submit', async function(e) {{
    e.preventDefault();
    const url = "/crearestudios/";

    const formData = new FormData(studiesForm);

    formData.forEach(function(value, key) {
        console.log(key, value);
    });

    axios.defaults.headers = {
      "Content-Type": "application/json",
      // 'X-CSRFToken': 'csrftoken',
    //   'content-type': 'multipart/form-data',
    }
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    axios({
        method: 'post',
        url: url,
        data: formData,
        // {
        //   name:data.name,
        //   sku:data.sku,
        //   }
      })
      .then( async (res) => {
        console.log(res.data);
        // alert("Informacion ingresada con Exito")
        console.log('Estado de la petición:', res.status);

        // if(res.status !== 200){
        //     throw new Error("Error")
        // }
        // throw new Error('No se puede dividir por cero');
        await swalconfirmation("Estudio creado con exito")
        window.location.replace("/listaempleado/")
      }).catch(async (e) => {
        console.error(e);
        await swalErr("No fue posible crear el registro de estudio para el empleado verifique la informacion.")
      })

    
}})



function crearEstudio() {
    const url = "/crearestudios/";
    let data = {
      num_documento: 0,
      anio: "",
      mes: "",
      estudio: "",
      institucion: "",
      titulo_obtenido: 0,
    };

    data.num_documento =  document.getElementById("num_documento").valueAsNumber;
    data.anio = document.getElementById("anio").value;
    data.mes = document.getElementById("mes").value;
    data.estudio = document.getElementById("estudio").value;
    data.institucion = document.getElementById("institucion").value;
    data.titulo_obtenido = document.getElementById("titulo_obtenido").value;


    const formData = new FormData();
    //console.log(name);
    formData.append('num_documento', data.num_documento);
    formData.append('anio', data.anio);
    formData.append('mes', data.mes);
    formData.append('estudio', data.estudio);
    formData.append('institucion', data.institucion);
    formData.append('titulo_obtenido',data.titulo_obtenido );
    console.log(data);


    axios.defaults.headers = {
      "Content-Type": "application/json",
      // 'X-CSRFToken': 'csrftoken',
      'content-type': 'multipart/form-data',
    }
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    axios({
        method: 'post',
        url: url,
        data: formData,
        // {
        //   name:data.name,
        //   sku:data.sku,
        //   }
      })
      .then(res => {
        console.log(res.data);
        alert("Informacion ingresada con Exito")
      })
  }
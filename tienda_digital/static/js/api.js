/*  Mudulo Api.js
Se crea coon la finalidad de modularizar las solicitudes fetch syncronas
debido a que el uso de fetch consume una alta cantidad de espacio que 
dificulta la lectura del codigo y por consiguiente el mantenimiento.

Este modulo se encargara de hacer las solicitudes Http   */

/* se obtiene csrftoken del modulo getCookie.js */
const csrftoken = getCookie('csrftoken');

/* Aqui se define la URL del proyecto*/
const URL = window.location.href
wl = URL.split("/");
// const Url = wl[0]+"//"+wl[2]+"/"+wl[3]+"/";
const BASE_URL = `${wl[0]}//${wl[2]}/`
console.log(BASE_URL);
        

async function callApi(endPoint, options = {}){
    options.headers = {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json',
      }
      //console.log(csrftoken)

    const url = BASE_URL + endPoint;
    const response =  await fetch(url, options);
    const data = await response.json();
    return {res: response, data: data}
}


async function callApiFile(endPoint, options = {}){
  options.headers = {
      'X-CSRFToken': csrftoken,
      'Content-Type': 'application/json',
    }
    //console.log(csrftoken)

  const url = BASE_URL + endPoint;
  //const response =  await fetch(url, options);

  // const request = new Request(
  //     Url,
  //     {
  //         method: 'POST',
  //         headers: {'X-CSRFToken': csrftoken},
  //         body: JSON.stringify(_datos),
  //         mode: 'same-origin', // Do not send CSRF token to another domain.
          
  //     }
  // );

  fetch(url,options).then((res) =>  {
      filename = res.headers.get("content-disposition");
      filename = filename.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)[1];
      /*filename = filename.split('%20').join(' '); */filename = filename.replace(/%20/g, " ");
      console.log(filename);
      return res.blob() })
  .then((data) => {
      var a = document.createElement("a")
      a.href = window.URL.createObjectURL(data)
      a.download = filename;
      a.click();
      //button.disabled = false;
      //button.classList.remove("btn-primary");
      //button.classList.add("btn-light");
      //spinner.hidden = true;
      
  })
  .catch((error) => {
      //button.disabled = false;
      //button.classList.remove("btn-primary");
      //button.classList.add("btn-light");
      //spinner.hidden = true;
      alert('Descarga de reporte Cancelada, Verifique conexión e intente nuevamente.');
      return
  })
  // const data = await response.json();
  // return {res: response, data: data}
  return
}
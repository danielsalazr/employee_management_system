const experienceForm = document.querySelector("form");

experienceForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(experienceForm);

  const n_documento = formData.get("n_documento");

  // printing formData elements
  formData.forEach((value, name) => {
    console.log(`${name}: ${value}`);
  });

  const url = `/empleados/experience/${n_documento}`;
  axios.defaults.headers = {
    "Content-Type": "application/json",
    "content-type": "multipart/form-data",
  };
  axios.defaults.xsrfCookieName = "csrftoken";
  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

  axios({
    method: "post",
    url: url,
    data: formData,
  })
    .then(async (res) => {
      console.log(res.data);
      swalconfirmationAndReload('Informacion ingresada con exito');
    })
    .catch(async (error) => {
      
      if (error.response.status == 404) {
        await swalErr("El numero de documento no coincide con ningun empleado");
      }
    });
});

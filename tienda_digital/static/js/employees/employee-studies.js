const num_documento = document.querySelector('#num_documento');
const anio ='';


num_documento.focus()

num_documento.addEventListener('blur', async () => {
    
    const url = `empleados/?id=${num_documento.value}`;
    const req = await callApi(url);

    console.log(req.res)
});
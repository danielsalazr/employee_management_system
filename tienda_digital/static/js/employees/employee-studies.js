const num_documento = document.querySelector('#num_documento');
const empleado = document.querySelector('#empleado');
const btnStudies = document.querySelector('#btnStudies');

const anio ='';


num_documento.focus()

num_documento.addEventListener('blur', async () => {
    
    const url = `empleados/?id=${num_documento.value}`;
    const req = await callApi(url);

    if (req.res.status !== 200){
        empleado.value =''
        btnStudies.disabled = true;
        await swalErr("No existe un empleado registrado con este numero de identidad")
    }

    

    console.log(req.res)
    console.log(req.data)
    const data =req.data[0]

    

    empleado.value = `${data.nombre} ${data.apellido}`
    btnStudies.disabled = false;
});
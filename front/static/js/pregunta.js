var btn = document.getElementById('preguntaControl'),
    contenido = document.getElementById('contenidoPregunta'),
    contenido2 = document.getElementById('contenidoPregunta2'),
    btnA = document.getElementById('respuestaControl'),
    contenidoA = document.getElementById('contenidoRespuesta'),
    contenidoA2 = document.getElementById('contenidoRespuesta2'),
    contador=0,
    contadorA=0;
 function cambio(){
     if(contador==0){
        contenido.classList.add('mostrar');
        contenido2.classList.add('mostrar');
        contador=1;
     }
     else{
         contenido.classList.remove('mostrar');
         contenido2.classList.remove('mostrar');
         contador=0;
     }
 }

 function cambioRespuesta(){
    if(contadorA==0){
       contenidoA.classList.add('mostrar');
       contenidoA2.classList.add('mostrar');
       contadorA=1;
    }
    else{
        contenidoA.classList.remove('mostrar');
        contenidoA2.classList.remove('mostrar');
        contadorA=0;
    }
}
btn.addEventListener('click',cambio,true)
btnA.addEventListener('click',cambioRespuesta,true)
### Gracias a José Luis Roberto Zárate Cortés por las siguientes instrucciones :)


### Sistema Operativo Windows 10 Home.

La instalación de Docker Desktop for Windows requiere Windows 10 64bit: Pro, Enterprise or Education
(Build 15063 o posterior).Para Windows 10 Home Edit., es necesario instalar:

[Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)

Esta solución utiliza una Oracle VM Virtual Box para ejecutar Docker

## Para montar un volumen

Es necesario apagar la machine `default` si está corriendo con:

```
docker-machine stop default
```

Y realizar los siguientes pasos para montar una carpeta (si no van a mapear puertos no es necesario ejecutar el `stop` de `docker-machine`).


1. Habilitar la opción de carpeta compartida para MONTAR en un directorio local, con lo que se direccionan los archivos creados en el contenedor a una carpeta evitando la pérdida en caso de borrado accidental del contenedor:
    

Abrir ORACLE VM VirtualBox e ir a:
  
Configuración-->Carpetas Compartidas-->Agregar (+). En el cuadro indicar Ruta Carpeta, Nombre y seleccionar los checklist Automontar y Hacer Permanente.
        
        

<img src="https://dl.dropboxusercontent.com/s/oieyklwb2u609vf/Img_docker_windows_virtual_box_1.png?dl=0" heigth="800" width="800">

<img src="https://dl.dropboxusercontent.com/s/kbdso5vly38q4cp/Img_docker_windows_virtual_box_2.png?dl=0" heigth="800" width="800">

<img src="https://dl.dropboxusercontent.com/s/gj8f370jrveso0f/Img_docker_windows_virtual_box_3.png?dl=0" heigth="800" width="800">


Es importante mencionar lo siguiente:

1. La ruta de la carpeta no debe contener caracteres especiales o nombres que el sistema traduce en la ruta pero no en el sistema, por ejemplo "Documents" por "Documentos".
    
2. Al montar en "dir_montar", para la ruta utilizada se eliminan los dos puntos `:` y se sustituye el símbolo diagonal invertida `\` por diagonal `/`, por ejemplo:
    
        dir_montar=C:\Users\miuser\folder
        dir_montar=/c/Users/miuser/Folder
                

2. Iniciar la máquina de default con un:

```
docker-machine start default
```

## Para reenvío de puertos

1. Reconfigurar el Reenvío de Puertos para tener JupyterLab de forma local y ejecutarlo desde un Browser:

Abrir ORACLE VM VirtualBox e ir a:
        
Configuración-->Red-->Avanzadas-->Reenvío de Puertos-->Agregar (+)

Finalmente, debemos registrar 8888 tanto en Puerto Anfitrión como en Puerto Invitado y Aceptar

<img src="https://dl.dropboxusercontent.com/s/0q8paonqvwq0ckl/Img_docker_windows_virtual_box_0.png?dl=0" heigth="800" width="800">


        
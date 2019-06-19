# Comandos a utilizar:


## Imágenes

Enlistar imágenes que tengo en mi sistema:

```
docker images
```

Descargar imágenes almacenadas en [dockerhub](https://hub.docker.com/): (no se deben colocar los símbolos `<`, `>`)

```
docker pull <imagen a descargar>:<version de imagen>
```

Borrar imagen:

```
docker rmi -f <imagen descargada>
```

## Run y exec

### Run 1

Crear contenedor con nombre `micontenedor` a partir de imagen de `ubuntu` (latest) que ejecute el comando `bash` en modo de `daemon`: (no se deben colocar los símbolos `<`, `>`)

```
docker run --name <micontenedor> -dit ubuntu bash
```

### Run 2

Crear contenedor con nombre `micontenedor` a partir de imagen de `ubuntu` (latest) que ejecute el comando `bash` en modo de `daemon` y se monte un volumen:

Primero elegimos el directorio que queremos montar, por ejemplo: `/home/<miuser>/<midirectorio>` y elegimos el nombre al que estará mapeado por ejemplo `/datos` 

(no se deben colocar los símbolos `<`, `>`)

```
dir_montar=/home/<miuser>/<midirectorio>
docker run -v $dir_montar:/datos --name <micontenedor> -dit ubuntu bash
```

### Run 3

Crear contenedor con nombre `micontenedor` a partir de imagen de `ubuntu` (latest) que ejecute el comando `bash` en modo de `daemon`, se monte un volumen y se use el puerto dentro del contenedor `puerto contenedor` mapeado al puerto de la máquina `puerto máquina`:

Primero elegimos el directorio que queremos montar, por ejemplo: `/home/<miuser>/<midirectorio>` y elegimos el nombre al que estará mapeado por ejemplo `/datos` 

(no se deben colocar los símbolos `<`, `>`)

```
dir_montar=/home/<miuser>/<midirectorio>
docker run -v $dir_montar:/datos --name <micontenedor> -p <puerto máquina>:<puerto contenedor> -dit ubuntu bash
```

### Exec (una vez ejecutado run anterior)

Entrar al contenedor `micontenedor`: (no se deben colocar los símbolos `<`, `>`)

```
docker exec -it <micontenedor> bash
```

y salimos con:

```
exit
```

Entrar al contenedor `micontenedor` con un user `miuser` creado: (no se deben colocar los símbolos `<`, `>`)


```
docker exec -u=<miuser> -it <micontenedor> /bin/bash
```

## ps, start, stop y rm

Al ejecutar un `docker run ...` se puede enlistar aquellos contenedores que están corriendo con:


```
docker ps
```

y este comando tiene la bandera `-a` para enlistar aquellos contenedores que están corriendo o están detenidos:


```
docker ps -a
```

Si algún contenedor está detenido y lo queremos iniciar (recordando que previamente hicimos una ejecución de `docker run`) realizamos: (no se deben colocar los símbolos `<`, `>`)

```
docker start <micontenedor>
```

Si por el contrario queremos detener un contenedor:

```
docker stop <micontenedor>
```

y si ya nunca más lo vamos a usar lo borramos con:


```
docker rm <micontenedor>
```




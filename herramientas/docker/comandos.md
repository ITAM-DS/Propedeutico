# Comandos a utilizar:


## Imágenes

Enlistar imágenes que tengo en mi sistema:

```
docker images
```

Descargar imágenes almacenadas en dockerhub:

```
docker pull <imagen>:<version>
```

Borrar imagen:

```
docker rmi -f <imagen>
```

## Run y exec

### Run 1

Crear contenedor con nombre `micontenedor` a partir de imagen de `ubuntu` (latest) que ejecute el comando `bash` en modo de `daemon`:

```
docker run --name micontenedor -dit ubuntu bash
```

### Run 2

Crear contenedor con nombre `micontenedor` a partir de imagen de `ubuntu` (latest) que ejecute el comando `bash` en modo de `daemon` y se monte un volumen:

Primero elegimos el directorio que queremos montar, por ejemplo: `/home/<miuser>/<midirectorio>` y elegimos el nombre al que estará mapeado por ejemplo `/datos`

```
dir_montar=/home/<miuser>/<midirectorio>
docker run -v $dir_montar:/datos --name micontenedor -dit ubuntu bash
```

### Exec (una vez ejecutado run anterior)

Entrar al contenedor `micontenedor`:

```
docker exec -it micontenedor bash
```

y salimos con:

```
exit
```







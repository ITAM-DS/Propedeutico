
# Imagen de docker

Lo que se necesita para correr los ejemplos del propedéutico es:

* Tener docker instalado en sus sistemas (ver [About Docker CE](https://docs.docker.com/install/)).
* Elegir un directorio que se montará en el contenedor (la ruta al directorio de su elección **no** debe tener espacios o caracteres como acentos, si desean separar las palabras usen guiones).
* Ejecutar lo siguiente:


```
dir_montar=<ruta completa a directorio> #aquí colocar la ruta al directorio a montar.

docker run -d -p 8787:8787 -v $dir_montar:/home/rstudio/ --name micontenedor-r -e PASSWORD=miprope palmoreck/prope_r:v1
```

y vamos a un browser y colocamos:

```
localhost:8787
```

Si quieren desde la terminal entrar a este contenedor sin Rstudio ejecuten en la terminal (una vez ejecutado el `run` anterior):


```
docker exec -it -u=rstudio propedeutico-r bash
```

**Obs:** la imagen `palmoreck/prope_r:v1` tiene `ggplot2` instalado. Alternativamente si desean tener una imagen de docker limpia usen:

```
dir_montar=<ruta completa a directorio> #aquí colocar la ruta al directorio a montar.
docker run -d -p 8787:8787 -v $dir_montar:/home/rstudio/ --name micontenedor-r-limpio -e PASSWORD=miprope rocker/rstudio
```

o pueden elegir la imagen de su preferencia aquí:

[rocker-org/rocker](https://github.com/rocker-org/rocker)

## Jupyterlab + R y python3

También si les gusta [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/) pueden descargar la imagen de docker para uso de `python3` y `R` desde `jupyterlab` ejecutando:

```
dir_montar=<ruta completa a directorio> #aquí colocar la ruta al directorio a montar.
docker run -v $dir_montar:/datos --name micontenedor-jupyterlab-python-r -dit -p 8889:8888 palmoreck/prope_jupyterlab_python_r:v1 bash
```

Entramos al contenedor con:

```
docker exec -it -u=miuser micontenedor-jupyterlab-python-r bash
```

Una vez dentro trabajamos en el ambiente propedeutico:

```
workon propedeutico
```

Si deseamos tener jupyterlab de forma local ejecutamos:

```
cd /

jupyter lab --ip=0.0.0.0 --no-browser --allow-root &
```

y vamos a un browser y colocamos:

```
localhost:8889
```

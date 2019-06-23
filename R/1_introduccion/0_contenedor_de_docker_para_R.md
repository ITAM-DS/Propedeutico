
Lo que se necesita para correr los ejemplos del propedéutico es:

* Tener docker instalado en sus sistemas (ver [About Docker CE](https://docs.docker.com/install/)).
* Elegir un directorio que se montará en el contenedor (la ruta al directorio de su elección **no** debe tener espacios o caracteres como acentos, si desean separar las palabras usen guiones).
* Ejecutar lo siguiente:


```
dir_montar=<ruta completa a directorio> #aquí colocar la ruta al directorio a montar.

docker run -d -p 8787:8787 -v $dir_montar:/home/rstudio/ --name propedeutico-r -e PASSWORD=miprope palmoreck/prope_r:v1
```

y vamos a un browser y colocamos:

```
localhost:8787
```

**Obs:** la imagen `palmoreck/prope_r:v1` tiene `ggplot2` instalado. Alternativamente si desean tener una imagen de docker limpia usen:

```
dir_montar=<ruta completa a directorio> #aquí colocar la ruta al directorio a montar.
docker run -d -p 8787:8787 -v $dir_montar:/home/rstudio/ --name propedeutico-r-limpio -e PASSWORD=miprope rocker/rstudio
```

o pueden elegir la imagen de su preferencia aquí:

[rocker-org/rocker](https://github.com/rocker-org/rocker)

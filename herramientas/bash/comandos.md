# Comandos a utilizar:


Básicos:

```
echo #para imprimir en pantalla: echo "hola mundo"
touch #para crear archivos: touch <miarchivo.txt o miarchivo.py o miarchivo.R>
mkdir #para crear directorios: mkdir <midirectorio>
cd #para entrar a directorios: cd <midirectorio>
cd .. #para salir del directorio actual
rm #para borrar archivos: rm <miarchivo> 
rm -r <midirectorio> #para borrar un directorio y los archivos debajo de éste
ls #para enlistar directorios: ls <midirectorio>
ls -lha #para enlistar directorios (o archivos) incluyendo archivos ocultos y el tamaño de archivos: ls -lha <midirectorio> o ls -lha <miarchivo>
docker #hay que instalar la herramienta docker
```

para AWS:

```
chmod 400 <millave.pem> #para establecer permisos de la llave
ssh -i <aquí colocar la llave .pem> -o ServerAliveInterval=60 ubuntu@<aquí colocar el Public DNS (IPv4) de la instancia> #para entrar a la instancia

```

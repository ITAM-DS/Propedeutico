# Comandos a utilizar:

Clonar un repo:

```
git clone <url de mi repo que está en gh-classroom> <aquí colocar nombre de un directorio>

#el comando anterior les pedirá sus credenciales de github tecleen la respuesta y den enter por cada respuesta

cd <nombre del directorio elegido en la línea anterior> 
#cd es "change directory" y lo usamos para entrar al directorio
```

Verificar si existen cambios que debo conseguir con `pull`:

```
git pull origin <rama> #por ejemplo rama master
```

Añadir un archivo y push al repo:

```
git config --global user.email "<mi correo asociado de github>"
git config --global user.name "<mi nombre>"
git add <nombre de mi notebook>
git commit -m "mensaje de mi commit" -i <nombre de mi archivo>
git push origin <rama> #por ejemplo rama master
```

La última línea les pedirá sus credenciales de github.

Después de realizar por primera vez lo anterior si quiero hacer cambios en un archivo el flujo que sigo es:


```
#clonar repo a un directorio si no lo tengo clonado
#entrar al directorio con cd
#git config --global user.email "<mi correo asociado de github>"
#git config --global user.name "<mi nombre>"
git commit -m "mensaje de mi commit con los cambios" -i <nombre de mi archivo>
git push origin <rama> #por ejemplo rama master
```

Si quiero borrar un archivo que ya fue añadido con `git add <nombre de mi archivo>` hago:

```
git rm <nombre de mi archivo>
```

y luego el commit, push correspondiente:

```
git commit -m "mensaje de commit" -i <nombre de mi archivo borrado>
git push origin <rama>
```


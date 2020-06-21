### Gracias a Aáron Torrijos Solís por las siguientes instrucciones :)

### Instalación en MS Windows 10

#### Previos

__Asegurate de__ tener la versión reciente de este SO (Actualizado a _version 2004_, _Build 19041_ o superior)
 
Puedes revisar la versión del SO de las maneras siguientes:

a. Presiona la tecla con el logo de windows (Win key) + R, escribe `winver`, y presiona aceptar:

<img src="https://dl.dropboxusercontent.com/s/giy7lohu3bcfpvo/forma_1a.jpg?dl=0" heigth="400" width="400">

<img src="https://dl.dropboxusercontent.com/s/0jikvb10ew18rih/forma_1b.png?dl=0" heigth="400" width="400">

b. Ingresa el comando `ver` en _Windows Command Prompt_:

<img src="https://dl.dropboxusercontent.com/s/sq9xssvcyroyxhw/forma_2.jpg?dl=0" heigth="400" width="400">


c. Ingresa a _Configuración_, después en _Acerca de_:

<img src="https://dl.dropboxusercontent.com/s/hv8amjfqmkbjci4/forma_3.jpg?dl=0" heigth="800" width="800">


#### Instalar subsistema WSL 2

Antes de instalar cualquier distribución de Linux, debes habilitar el subsistema _WSL_ (_Windows Subsystem for Linux_)

1. Abre _PowerShell_ con privilegios de adminstrador y ejecuta:

    ```
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    ```

2. Reinicia tu máquina
3. Establece _WSL 2_ (versión 2 de _WSL_) como la versión por defecto, para eso ejecuta en _PowerShell_ el comando siguiente:

    ```
    wsl --set-default-version 2
    ```
    i. Si aparece el mensaje `WSL 2 requires an update to its kernel component. For information please visit https://aka.ms/wsl2kernel` visita la página [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)
    
    ii. Instala la actualización _WSL 2 Linux kernel_,
    también lo puedes descargar desde: [https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
    
4. Abre la tienda de aplicaciones de Microsoft (_Microsoft Store_) e instala la distribución Linux de tu interés. Están disponibles:
    * [Ubuntu 16.04 LTS](https://www.microsoft.com/store/apps/9pjn388hp8c9)
    * [Ubuntu 18.04 LTS](https://www.microsoft.com/store/apps/9N9TNGVNDL3Q)
    * [Ubuntu 20.04 LTS](https://www.microsoft.com/store/apps/9n6svws3rx71)
    * [openSUSE Leap 15.1](https://www.microsoft.com/store/apps/9NJFZK00FGKV)
    * [SUSE Linux Enterprise Server 12 SP5](https://www.microsoft.com/store/apps/9MZ3D1TRP8T1)
    * [SUSE Linux Enterprise Server 15 SP1](https://www.microsoft.com/store/apps/9PN498VPMF3Z)
    * [Kali Linux](https://www.microsoft.com/store/apps/9PKR34TNCV07)
    * [Debian GNU/Linux](https://www.microsoft.com/store/apps/9MSVKQC78PK6)
    * [Fedora Remix for WSL](https://www.microsoft.com/store/apps/9n6gdm4k2hnc)
    * [Pengwin](https://www.microsoft.com/store/apps/9NV1GV1PXZ6P)
    * [Pengwin Enterprise](https://www.microsoft.com/store/apps/9N8LP0X93VCP)
    * [Alpine WSL](https://www.microsoft.com/store/apps/9p804crf0395)
    
5. La distribución funcionará como un programa más, corre la distribución y configurala para su primer uso.

    i. La primera vez que corre la distribución, una consola te pedirá que esperes unos minutos para completar la instalación.
    
    ii. Te pedira que crees un usuario, lo único que tienes que hacer es teclear el nombre de usario que deseas y presiona la tecla 'enter'.
    
    iii. Te pedira que crees una contraseña para este usuario, teclea la contraseña que deseas y presiona la tecla 'enter'. Te solicitará que la confirmes y presiona la tecla 'enter' nuevamente.
    
<img src="https://dl.dropboxusercontent.com/s/smavjnefg0e1jbu/ubuntuinstall.png?dl=0" heigth="800" width="800">


6. Descarga e instala [docker](https://www.docker.com/get-started).

7. En algún momento durante la instalación, si ya estás corriendo un sistema que soporte _WLS 2_, docker activara _WSL 2_ o te pedirá que marques una casilla para activarlo. Lee la información desplegada y activa _WSL 2_ para continuar.
8. Si ya tenias instalado docker y después instalaste _WSL 2_ desde el menú de configuraciones lo puedes activar, selecciona `Settings > General`.

<img src="https://dl.dropboxusercontent.com/s/l64oj536zfrlqq3/wsl2-enable.png?dl=0" heigth="800" width="800">

        
#### Referencias.

* [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* [https://docs.docker.com/docker-for-windows/wsl/](https://docs.docker.com/docker-for-windows/wsl/)
* [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)
* [https://www.docker.com/get-started](https://www.docker.com/get-started)
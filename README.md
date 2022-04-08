# Laboratorio 1 - Robótica - 2022-I
### Integrantes
- Nicolas Pulido Gerena
- Santiago Sanchez

## Conexión de ROS con Matlab
Usando la sintaxis de Matlab se implemento la funciòn con los argumentos: nombre de nodo y el tipo de mensaje.
Una vez sr haya hecho la subscripciòn al nodo se puede acceder al ultimo mensaje haciendo uso de LatestMessage.
[![Captura-de-pantalla-de-2022-04-07-22-35-20.png](https://i.postimg.cc/5ts7G5kf/Captura-de-pantalla-de-2022-04-07-22-35-20.png)](https://postimg.cc/WDJwqZvy)

Finalmente para terminar la conexion al nodo maestro se usa la siguiente linea de codigo.
[![Captura-de-pantalla-de-2022-04-07-22-35-20-1.png](https://i.postimg.cc/Y26gC2MW/Captura-de-pantalla-de-2022-04-07-22-35-20-1.png)](https://postimg.cc/G9p9MCBL)
## Script de Python
Se utilizó la libreria "pynput.keyboard" para poder realizar la detección del teclado y con eso se hace la definición de las funciones "on_press" y "on_release" para  habilitar condicionales de las teclas segun la acción deseada.

Para las teclas A, S, D, W, se utilizó el topico "turtle1/cmd vel" y para las teclas R y ESPACIO se utilizaron los servicios "turtle1/teleport absolute" y "turtle1/teleport relative".

Adicionalmente, se añadió el script de python en el apartado de "catkin_install_python" del archivo "CMakeLists.txt"

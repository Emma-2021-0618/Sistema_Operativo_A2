# UCATECI
- Sistemas operativo 2
- Lizandro jose Ramirez
- Encuentro 7 Teoria

# Tema
- Problema del barbero durmiente

# Autores
- Enmanuel Sanchez Rodriguez 2021-0618
- Albert Francisco Hernandez Sanchez 2019-0126

# Desarrollo

Importamos la librerias:
~~~
import threading
import time
import random
from multiprocessing import Process, Queue, cpu_count
~~~

Aquí estan todas las librerias que usaremos desde la importacion de la libreria de hilos, el tiempo, el uso de numeros pseudo-aleatorios
y procesos, colas y contador de cpu desde multi-procesamiento.

Definimos al barbero:
~~~

def barber(queue):
    while True:
        queue.get()
        print("El barbero esta cortando cabello")
        time.sleep(random.randint(10, 25)) 
~~~

Definimos al barbero con una cola la cual definira sus paramentros la obtenemos, imprimos el mensaje del estado del barbero y luego tenemos un tiempo
en el cual, el barbero esta cortando el pelo.

Definimos al cliente:
~~~
def customer(queue):
    while True:
	    print("el cliente esta en la sala de espera")
	    queue.put('Work')
	    time.sleep(random.randint(1, 3))

~~~

Definimos al cliente el cual entrar a sala en forma de mensaje y pone le cola una un interancion la cual la puede ver el barbero y al final ponemos 
el tiempo que dura cada cliente en venir del 1 al 3.


{}[Video explicandolo]

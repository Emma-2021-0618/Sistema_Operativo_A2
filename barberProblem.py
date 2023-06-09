import threading
import time
import random
from multiprocessing import Process, Queue, cpu_count


def barber(queue):
    while True:
        queue.get()
        print("El barbero esta cortando cabello")
        time.sleep(random.randint(10, 25))

def customer(queue):
	while True:
	    print("el cliente esta en la sala de espera")
	    queue.put('Work')
	    time.sleep(random.randint(1, 3))


class Manager:
    def __init__(self):
        self.queue = Queue()
        self.NUMBER_OF_PROCESSES = cpu_count()

    def start(self):
        self.workers = [Process(target=barber, args=(self.queue,)) for i in range(self.NUMBER_OF_PROCESSES)]
        for w in self.workers:
            w.start()

        customer(self.queue)

    def stop(self):
        self.queue.put(None)
        for i in range(self.NUMBER_OF_PROCESS):
            self.workers[i].join()
        self.queue.close()


Manager().start()

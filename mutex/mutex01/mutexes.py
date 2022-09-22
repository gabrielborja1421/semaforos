from concurrent.futures import thread
from threading import Thread
import threading
from time import sleep

mutex= threading.Lock()

class Hilo(threading.Thread)
    def __init__(self, id):
            threading.Thread.__init__(self)
            self.id=id
    def run(self):
        mutex.acquire()
        sleep(3-self.id)
        crito(id)
        # print("valor"+ str(self.id))
        mutex.release()
        

url=["https://youtu.be/2iVf6CtcasQ","https://youtu.be/COd37qgfwcc","https://youtu.be/m6jfZa00vkY","https://youtu.be/Wi8zGmkz6N0","https://youtu.be/fGxcXLDoiYM","https://youtu.be/o5obzbQnl1M","https://youtu.be/OtUy4QQS4jE","https://youtu.be/iy1eqIKNoBk","https://youtu.be/cN9VkgRDdXI","https://youtu.be/R8Lv6HPDR3A"]

hilos = [Hilo(1), Hilo(2), Hilo(3),Hilo(4),Hilo(5),Hilo(6),Hilo(7),Hilo(8),Hilo(9),Hilo(10)]
x=1;
for h in hilos:
    h.start()
    
def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1
    
    # get_service(id)
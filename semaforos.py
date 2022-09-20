from threading import Thread, Semaphore
from turtle import st
import pytube 
semaforo = Semaphore(1)

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1
    
    get_service(id)

def get_service(id):
    print('si pasa')
    j=-1
    j=j+ id   
    print(j)
    yt = pytube.YouTube(url[j])
    yt.streams.first().download()
class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id
   

    def run(self):
        semaforo.acquire()
        crito(self.id)
        
        semaforo.release()

        
        
        

url=["https://youtu.be/2iVf6CtcasQ","https://youtu.be/COd37qgfwcc","https://youtu.be/m6jfZa00vkY","https://youtu.be/Wi8zGmkz6N0","https://youtu.be/fGxcXLDoiYM","https://youtu.be/o5obzbQnl1M","https://youtu.be/OtUy4QQS4jE","https://youtu.be/iy1eqIKNoBk","https://youtu.be/cN9VkgRDdXI","https://youtu.be/R8Lv6HPDR3A"]

threads_semaphore = [Hilo(1), Hilo(2), Hilo(3),Hilo(4),Hilo(5),Hilo(6),Hilo(7),Hilo(8),Hilo(9),Hilo(10)]
x=1;
for t in threads_semaphore:
    t.start()
    


    


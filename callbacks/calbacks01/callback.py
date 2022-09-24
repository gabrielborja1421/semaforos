from ast import keyword
from socket import SO_VM_SOCKETS_BUFFER_MIN_SIZE
from typing_extensions import Self
from urllib import response
import requests,threading

def get_service1():
    pass
def get_error1():
    pass
def request_data(url):
    response= requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else
        error_callback

class Hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        def run(self)
        h1=threading.Thread(target=request_data,
        kwargs={
            'url':''
            'success_callback':,
        })
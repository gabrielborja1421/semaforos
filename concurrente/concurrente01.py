import requests
import concurrent.futures
import threading
import time
import psycopg2

threading_local = threading.local()

conexion = psycopg2.connect(user='postgres', password='14211421', host='localhost', port='5432', database='concurrente')
cursor = conexion.cursor()



def get_service(url):
    response = requests.get(url)
    
    write_db(response.json().get('results'))


def write_db(x):
    for i in x:
        cursor.execute("INSERT INTO names(name) VALUES('"+ i['name']['first'] +"')")
        conexion.commit() 
        


if __name__ == "__main__":
    start_time = time.time()
    get_service('https://randomuser.me/api/?results=2000')
    end_time = time.time()
    print(end_time - start_time)
    conexion.close()
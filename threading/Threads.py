import requests
import threading
import pytube 
import concurrent.futures
import time
import psycopg2

lock = threading.Lock()
# concurrente
threading_local = threading.local()
def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_services)

#obtener usuarios
def get_users(x=0):
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)
# obtener videos
def get_media():
    
    yt = pytube.YouTube("https://youtu.be/44XYEeD1A1U")
    yt.streams.first().download()
    yt = pytube.YouTube("https://youtu.be/Wi8zGmkz6N0")
    yt.streams.first().download()
    yt = pytube.YouTube("https://youtu.be/bjGQj9PYjvg")
    yt.streams.first().download()
    yt = pytube.YouTube("https://youtu.be/rXpB_vJgDl0")
    yt.streams.first().download()
    yt = pytube.YouTube("https://youtu.be/N5-XXckaufY")
    yt.streams.first().download()
#obtener registros
def get_services():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=8"
    r = requests.get(url)
    data = r.json().get('results')
    i=0
    for e in data:
        nombres= data[i].get('name')
        print(nombres)
        i +=1
        write(nombres)
    pass



#ESCRIBIR EN LA BDD
def write(x):
    try:
        cursor1.execute("insert into pokemon (name) values ('"+x+"')")
    except Exception as err:
        print('Error en la inserción: ' + err)
    else:
        conexion.commit()
    pass
#CONNEXION A LA BDD
try:
    conexion = psycopg2.connect(database='concurrente', user='postgres', password='14211421')
    cursor1 = conexion.cursor()
    cursor1.execute('select version()')
    version = cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')
# FINALIZAR CONEXION CON BASE DE DATOS
def endConexion():
    conexion.close()
    pass



if __name__ == "__main__":
    start_time = time.time()

    thread1 = threading.Thread(target=get_services)
    thread2 = threading.Thread(target=get_media())

    thread1.start()
    thread2.start()
    
    for i in range(50):
        thread3 = threading.Thread(target=get_users)
        thread3.start()
        thread3.join()

    end_time = time.time()
    print(end_time - start_time)
    
#actividad 3 subprocesos
# descargar 5 videos
# escribir en bbd por lo menos 2000 registros
# generar una solicitud a ramdom users de por lo menos 50 usuarios 
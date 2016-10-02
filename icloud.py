#/usr/bin/python

from pyicloud import PyiCloudService
import time
import collections
import MySQLdb

DB_HOST = 'DB_HOST' 
DB_USER = 'DB_USER' 
DB_PASS = 'DB_PASS' 
DB_NAME = 'DB_NAME' 
 
def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexion 
 
    return data

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data	

def seldevice(api):
    
    dispositivos=convert(api.devices)
    if 1==len(list(dispositivos.values())):
        return api.devices[0]
    else:
        print("No soporta multiples dispositivos")
        #print("Elige un dispositivo")
        #i=0
        #for valor in convert(api.devices):
        #    i=i+1
        #    print "[%s]  -->  %s " % (i,valor)

def main(email,password,delay=3):
    api = PyiCloudService(email, password)
    

    timeunix=0
    device=seldevice(api)
    dispositivo=convert(device.status()).get("name")
    while True:
        loc=device.location()
        loc=convert(loc)
        if timeunix!=loc.get("timeStamp"):
            timeunix=loc.get("timeStamp")
            lat=loc.get("latitude")
            longi=loc.get("longitude")
            prec=loc.get("horizontalAccuracy")
            	
            query = "INSERT INTO loc (time, latitud, longitud, prec, cuenta, dispositivo) VALUES ('%s','%s','%s','%s','%s','%s')"%(str(timeunix),str(lat),str(longi),str(prec),str(email),str(dispositivo))
            print(query)
            run_query(query)
        time.sleep(delay)

main("email","pass","delay gps")

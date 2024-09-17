import requests
import csv
import json
from api_key import api_key

ciudad = input("Ingrese la Ciudad: ") 

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&lang=es"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    json_data = respuesta.json()
    
    l = json_data['location']
    c = json_data['current']
    
    ciudad = l['name']
    region = l['region']
    pais = l['country']
    temperatura_actual = c['temp_c']
    condicion_actual = c['condition']['text']
    precipitacion = c['precip_mm']
    humedad = c['humidity']
    fecha_actualizacion = c['last_updated']
    
    formato = input("formato deseas los datos? (json/csv): ")
    
    if formato == "json":
        datos_resu = {
            "ciudad": ciudad,
            "region": region,
            "pais": pais,
            "temperatura_actual": temperatura_actual,
            "condicion_actual": condicion_actual,
            "precipitacion": precipitacion,
            "humedad": humedad,
            "fecha_actualizacion": fecha_actualizacion,
        }
        print(json.dumps(datos_resu, indent=4))
        
    elif formato == "csv":
        with open('datos_clima.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(["ciudad", "region", "pais", "temperatura_actual", "condicion_actual", "precipitacion", "humedad", "fecha_actualizacion"])
            writer.writerow([ciudad, region, pais, temperatura_actual, condicion_actual, precipitacion, humedad, fecha_actualizacion])
        print("Datos guardados en 'datos_clima.csv'")
    else:
        print("Formato no valido, elige json o csv")
else:
    print(f"Error: {respuesta.status_code}")

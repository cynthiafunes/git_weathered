import requests
import requests.exceptions
from api_key import api_key


def obtener_datos_clima(ciudad):
    base_url = "http://api.weatherapi.com/v1/current.json?"
    params = {"key": api_key, "q": ciudad, "lang": "es"}

    try:
        respuesta = requests.get(base_url, params=params)
        print(f"{respuesta.url}")

        if respuesta.status_code == 200:
            json_data = respuesta.json()

            location = json_data["location"]
            current = json_data["current"]

            return {
                "ciudad": location["name"],
                "region": location["region"],
                "pais": location["country"],
                "temperatura_actual": current["temp_c"],
                "condicion_actual": current["condition"]["text"],
                "precipitacion": current["precip_mm"],
                "humedad": current["humidity"],
                "fecha_actualizacion": current["last_updated"],
            }

        elif respuesta.status_code == 400:
            raise Exception(f"Ubicacion no encontrada: {ciudad}")
        else:
            raise Exception(f"Error: {respuesta.status_code}")

    except requests.exceptions.ConnectionError:
        raise Exception("Error de conexion")

import requests
import requests.exceptions
from api_key import api_key


def obtener_datos_clima(ciudad):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&lang=es"

    try:
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            json_data = respuesta.json()

            if "error" in json_data:
                raise Exception(f"Ubicacion no encontrada: {ciudad}")

            location = json_data["location"]
            c = json_data["current"]

            return {
                "ciudad": location["name"],
                "region": location["region"],
                "pais": location["country"],
                "temperatura_actual": c["temp_c"],
                "condicion_actual": c["condition"]["text"],
                "precipitacion": c["precip_mm"],
                "humedad": c["humidity"],
                "fecha_actualizacion": c["last_updated"],
            }
        else:
            raise Exception(f"Error: {respuesta.status_code}")

    except requests.exceptions.ConnectionError:
        raise Exception("Error de conexion")


if __name__ == "__main__":
    ciudad_prueba = input("Ingrese la ciudad para probar la API: ")
    try:
        datos = obtener_datos_clima(ciudad_prueba)
        print(datos)
    except Exception as e:
        print(f"Error: {e}")

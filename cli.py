import argparse
import json
import csv
import sys
from api import obtener_datos_clima

def main():
    parser = argparse.ArgumentParser(description="Cli para la obtencion de datos climaticos")
    parser.add_argument("ciudad", help="Nombre de la ciudad")
    parser.add_argument("formato", choices=["json", "csv"], help="Formato de salida (json o csv)")
    
    args = parser.parse_args()
    
    ciudad = args.ciudad
    formato_salida = args.formato
    
    print(f"Obtener el clima de {ciudad} en {formato_salida}")

    datos_clima = obtener_datos_clima(ciudad)
    
    if formato_salida == "json":
        print(json.dumps(datos_clima, indent=2))
    else:  
        writer = csv.DictWriter(sys.stdout, fieldnames=datos_clima.keys())
        writer.writeheader()
        writer.writerow(datos_clima)

if __name__ == "__main__":
    main()
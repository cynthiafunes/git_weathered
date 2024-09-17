import argparse
import json
import csv
import sys

def main():
    parser = argparse.ArgumentParser(description="Cli para la obtencion de datos climaticos")
    parser.add_argument("ciudad", help="Nombre de la ciudad")
    parser.add_argument("formato", choices=["json", "csv"], help="Formato de salida (json o csv)")
    
    args = parser.parse_args()
    
    ciudad = args.ciudad
    formato_salida = args.formato
    
    print(f"Obtener el clima de {ciudad} en {formato_salida}")
    
    # despues voy a reemplazar esto
    data = {
        "ciudad": ciudad,
        "temperatura": 25,
        "condicion_actual": "Soleado",
        "humedad": 60
    }
    
    if formato_salida == "json":
        print(json.dumps(data, indent=2))
    else:  
        writer = csv.DictWriter(sys.stdout, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

if __name__ == "__main__":
    main()
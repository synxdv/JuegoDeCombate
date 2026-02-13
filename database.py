import json

try:
    with open("datos.json", "r") as f:
        datos = json.load(f)

except FileNotFoundError:
    datos = []

def guardar_datos():
    with open("datos.json", "w") as f:
        json.dump(datos,f, indent=4)
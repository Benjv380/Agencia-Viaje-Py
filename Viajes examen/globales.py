import json
import csv
import globales

def seleccionar_opcion(max_value):
    opcion = 0
    while True:    
        try:
            opcion = int(input("ingrese una opcion >>"))

        except:
            pass

        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion

def leer_archivo_json(dir):
    try:
        with open(dir, 'r') as archivo: # leemos el archivo
            return json.load(archivo) # retornamos lo que quenga el archivo
    except:
        return []

def guardar_archivo_json(dir, data):
    try:
        with open(dir, 'w') as archivo: # leemos el archivo
            json.dump(data, archivo, indent=4)
    except:
        return []

def leer_archivo_csv(dir):
    try:
        with open(dir, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []

def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode='w', newline='', encoding='utf-8') as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []
import globales, estadisticas
import random
import os
import json

def menu_geeneral():
    while True:
        print("1.	Asignar costos aleatorios a los destinos")
        print("2.	Clasificar destinos por costo")
        print("3.	Ver estadísticas de reservas")
        print("4.	Reporte de reservas")
        print("5.	Salir del programa")

        opcion = globales.seleccionar_opcion(5)
        try:    
            if opcion == 1:
                asignar_costos()
                os.system("cls")
            elif opcion == 2:
                os.system("cls")
                clasificar_viajes()
            elif opcion == 3:
                print("1. Promedio")
                print("2. Media Geometrica")
                print("3. Viaje mas caro")
                print("4. Viaje mas barato")
                print("0. Salir")
                opcion1 = globales.seleccionar_opcion(5)
                if opcion1 == 1:
                    estadisticas.promedio()
                elif opcion1 == 2:
                    estadisticas.media_geometrica()
                elif opcion1 == 3:
                    estadisticas.venta_alta()
                elif opcion1 == 4:
                    estadisticas.venta_baja()
                elif opcion1 == 5:
                    break
                    
            elif opcion == 4:
                reporte_de_reservas()
            elif opcion == 5:
                return
            input()
        except:
            os.system("cls")
            input("no ha generado archivo Json.")
            os.system("cls")

def asignar_costos():
    destinos = ["París",
                 "Londres",
                  "Nueva York",
                    "Tokio",
                      "Sídney", 
                        "Roma",
                         "Berlín",
                            "Barcelona"
                ]

    pasajeros = ["Juan Pérez",
                    "María García",
                     "Carlos López",
                        "Ana Martínez",
                          "Pedro Rodríguez",

            ]   
    
    nuevo_destino = []

    for i in pasajeros:
        x1 = random.choice(destinos)
        x = random.randint(100,1000) #costo
        cp = random.randint(1,10) #cant pasajero
        x2 = cp * x
        

        nuevo_viaje = {
            "nombre pasajero": i,
            "destino": x1,
            "costo pasaje": x,
            "cantidad de pasajeros": cp,
            "costo total": x2
        }

        nuevo_destino.append(nuevo_viaje)
    globales.guardar_archivo_json('pasajes.json', nuevo_destino)
    input("viajes cargados")

def clasificar_viajes():
    todos_los_viajes = globales.leer_archivo_json('pasajes.json')

    categorias = {
        'menores a $300': [],
        'entre $301 y $700': [],
        'sobre $701': []
    }

    for viaje in todos_los_viajes:
        if viaje['costo total'] <= 300:
            categorias["menores a $300"].append(viaje)
        elif viaje['costo total'] > 301 and viaje['costo total'] <= 700:
            categorias["entre $301 y $700"].append(viaje)
        elif viaje['costo total'] >= 701:
            categorias["sobre $701"].append(viaje)
    
    for clave, valor in categorias.items():
        print("------------------------------")
        print(f"{clave} >> {len(valor)} ")
        print("------------------------------")
        print("Nombre del destino       Costo")

        for precio in valor:
            print(f"{precio['destino']} \t\t ${precio['costo total']}")


def reporte_de_reservas():
    todoslosviajes = globales.leer_archivo_json('pasajes.json')

    print("---------------------------------------------------------------------------")
    print("| Nombre cliente | Destino Turistico | Cantidad de personas | Costo total |")
    print("---------------------------------------------------------------------------")

    for viaje in todoslosviajes:
        print(f"{viaje['nombre pasajero']} \t {viaje['destino']} \t {viaje['cantidad de pasajeros']} \t {viaje['costo total']}")

    fieldnames = ['nombre pasajero', 'destino', 'cantidad de pasajeros', 'costo total']
    globales.guardar_archivo_csv('reporte_reservas.csv', todoslosviajes ,fieldnames)

# reporte_de_reservas()



menu_geeneral()
# clasificar_viajes()
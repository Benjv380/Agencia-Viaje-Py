import math 
import globales

def venta_alta():
    ventas=globales.leer_archivo_json('ventas.json')
    ventas_ordenadas=sorted(ventas, key=lambda x:x ['total producto'], reverse= True)

    for venta in ventas_ordenadas[:1]:
        print(f"el valor mas alto de producto es :$ {venta['total producto']}")

def venta_baja():
    ventas=globales.leer_archivo_json('ventas.json')
    ventas_ordenadas=sorted(ventas, key=lambda x:x ['total producto'], reverse= False)

    for venta in ventas_ordenadas[:1]:
        print(f"el valor mas bajo de producto es :$ {venta['total producto']}")

def promedio():
    ventas=globales.leer_archivo_json('ventas.json')
    suma_ventas = 0
    toda_venta = 0

    for venta in ventas:
        suma_ventas = venta['total producto']
        toda_venta+=1

    promedio= suma_ventas/toda_venta

    print(f"{promedio}")

def media_geometrica():
    ventas=globales.leer_archivo_json('ventas.json')
    suma_ventas = 0
    toda_venta = 0

    for venta in ventas:
        suma_ventas = math.log(venta['total producto'])
        toda_venta+=1

    promedio= (math.exp(suma_ventas/toda_venta))

    print(f"{promedio}")

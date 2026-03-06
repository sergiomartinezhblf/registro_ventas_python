from datetime import datetime
import csv 
import os

ARCHIVO = "ventas.csv"

def registrar_venta():
    inicializar_archivo()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))

    total = cantidad*precio

    with open(ARCHIVO, "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([fecha,producto,cantidad,precio,total])
    
    print("Venta registrada correctamente")

def ver_ventas():
    inicializar_archivo()

    try:
        with open(ARCHIVO,"r") as archivo:
            lector = csv.reader(archivo)

            encabezado = next(lector)

            print("\n===HISTORIAL DE VENTAS===")
            print(f"{encabezado[0]:20} {encabezado[1]:15} {encabezado[2]:10}  {encabezado[3]:10} {encabezado[4]:10}")
            print("_"*60)

            hay_datos = False

            for fila in lector:
                if not fila:
                    continue
                
                hay_datos = True
                print(f"{fila[0]:20} {fila[1]:15} {fila[2]:10} {fila[3]:10} {fila[4]:10}")

            if not hay_datos:
                print("No hay ventas registradas")

    
    except FileNotFoundError:
        print("No hay ventas registradas")


def analizar_ventas():
    if not os.path.exists(ARCHIVO):
        print("No hay ventas registradas")
        return
    
    with open(ARCHIVO,"r") as archivo:
        lector = csv.DictReader(archivo)

        resumen = {}

        for fila in lector:
            producto = fila["producto"]
            cantidad = int(fila["cantidad"])
            total = float(fila["total"])

            if producto not in resumen:
                resumen[producto] = {
                    "cantidad": 0,
                    "ingreso": 0
                }
            
            resumen[producto]["cantidad"] += cantidad
            resumen[producto]["ingreso"] += total

        print("\n---ANALIS DE VENTAS---\n")
        print(f"{'PRODUCTO':20} {'CANTIDAD':20} {'INGRESO TOTAL':20}")

        for producto,datos in resumen.items():

            print(
                f"{producto:20}"
                f"{datos['cantidad']:20}"
                f"{datos['ingreso']:20}"
            )            

def inicializar_archivo():
    if not os.path.exists(ARCHIVO):

        with open(ARCHIVO, "w", newline="") as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow(["fecha","producto","cantidad","precio","total"])
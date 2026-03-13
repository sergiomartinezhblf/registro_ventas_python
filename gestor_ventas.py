from datetime import datetime
import csv 
import os
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

ARCHIVO = "ventas.csv"

def generar_reporte_pdf(ventas, analisis):

    # Crear el documento PDF con tamaño de página tipo carta
    pdf = SimpleDocTemplate("reporte_ventas.pdf", pagesize=letter)

    # Obtener estilos de texto predefinidos (título, encabezados, etc.)
    styles = getSampleStyleSheet()

    # Lista donde se irán agregando los elementos del PDF
    elementos = []

    # Crear el título principal del reporte
    titulo = Paragraph("Reporte de Ventas", styles["Title"])

    # Agregar el título a la lista de elementos
    elementos.append(titulo)

    # Agregar un espacio vertical después del título
    elementos.append(Spacer(1,20))


    # -------- TABLA DE VENTAS --------

    # Crear subtítulo para la sección de ventas
    subtitulo1 = Paragraph("Tabla de Ventas", styles["Heading2"])

    # Agregar subtítulo al documento
    elementos.append(subtitulo1)

    # Espacio después del subtítulo
    elementos.append(Spacer(1,10))

    # Crear la tabla con los datos de ventas
    tabla_ventas = Table(ventas)

    # Aplicar estilos visuales a la tabla
    tabla_ventas.setStyle(TableStyle([
        # Color de fondo de la primera fila (encabezados)
        ("BACKGROUND",(0,0),(-1,0),colors.grey),

        # Color del texto en encabezados
        ("TEXTCOLOR",(0,0),(-1,0),colors.whitesmoke),

        # Dibujar líneas de la cuadrícula de la tabla
        ("GRID",(0,0),(-1,-1),1,colors.black)
    ]))

    # Agregar tabla de ventas al documento
    elementos.append(tabla_ventas)

    # Espacio entre tablas
    elementos.append(Spacer(1,30))


    # -------- TABLA DE ANÁLISIS --------

    # Crear subtítulo para la sección de análisis
    subtitulo2 = Paragraph("Análisis de Ventas", styles["Heading2"])

    # Agregar subtítulo al documento
    elementos.append(subtitulo2)

    # Espacio después del subtítulo
    elementos.append(Spacer(1,10))

    # Crear tabla con los datos de análisis
    tabla_analisis = Table(analisis)

    # Aplicar estilos visuales a la tabla
    tabla_analisis.setStyle(TableStyle([
        # Dibujar líneas de la tabla
        ("GRID",(0,0),(-1,-1),1,colors.black),

        # Fondo gris para encabezados
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
    ]))

    # Agregar la tabla de análisis al documento
    elementos.append(tabla_analisis)

    # -------- GRAFICA DE VENTAS --------

    subtitulo3 = Paragraph("Gráfica de Ventas", styles["Heading2"])
    elementos.append(subtitulo3)

    elementos.append(Spacer(1,10))

    grafica = Image("grafica_ventas.png", width=400, height=250)

    elementos.append(grafica)

    # Construir finalmente el PDF con todos los elementos agregados
    pdf.build(elementos)

    # Mensaje en consola confirmando que el PDF fue generado
    print("Reporte PDF generado correctamente.")

    # Abre el PDF automaticamente una vez generado
    os.system("explorer.exe reporte_ventas.pdf")


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

def obtener_ventas():
    ventas = []
    inicializar_archivo()

    try:

        with open(ARCHIVO, newline="", encoding="utf-8")as archivo:
           lector = csv.reader(archivo)
           encabezado = next(lector)
           ventas.append(encabezado)

           for fila in lector:
                    fecha = fila[0]
                    producto = fila[1]
                    cantidad = fila[2]
                    precio = fila[3]
                    total = fila[4]
            
                    ventas.append([fecha,producto,cantidad,precio,total])
        return ventas

    except FileNotFoundError:
            print("No hay ventas registradas")

def ver_ventas():
    ventas = obtener_ventas()

    iterador = iter(ventas)
    encabezado = next(iterador)

    print("\n===HISTORIAL DE VENTAS===")
    print(f"{encabezado[0]:20} {encabezado[1]:15} {encabezado[2]:10}  {encabezado[3]:10} {encabezado[4]:10}")
    print("_"*60)

    hay_datos = False

    for fila in iterador:
        if not fila:
            continue
                
        hay_datos = True
        print(f"{fila[0]:20} {fila[1]:15} {fila[2]:10} {fila[3]:10} {fila[4]:10}")

    if not hay_datos:
        print("No hay ventas registradas")

def calcular_analisis_ventas():
    analisis = []
    analisis.append(["producto","cantidad","precio"])
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
        
        for producto,datos in resumen.items(): 

            analisis.append([producto,datos['cantidad'],datos['ingreso']])  
    
        return analisis


def analizar_ventas():
    analisis = calcular_analisis_ventas()
    iterador = iter(analisis)
    encabezado = next(iterador)

    print("\n---ANALIS DE VENTAS---\n")
    print(f"{'PRODUCTO':20} {'CANTIDAD':20} {'INGRESO TOTAL':20}")

    for fila in iterador:

        print(
            f"{fila[0]:20}"
            f"{fila[1]:20}"
            f"{fila[2]:20}"
            )      


def inicializar_archivo():
    if not os.path.exists(ARCHIVO):

        with open(ARCHIVO, "w", newline="") as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow(["fecha","producto","cantidad","precio","total"])
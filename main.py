from gestor_ventas import registrar_venta,ver_ventas,obtener_ventas,calcular_analisis_ventas,analizar_ventas,generar_reporte_pdf
from graficas import generar_grafica_ventas

def menu():
    while True:
        print("===SISTEMA DE REGISTRO DE VENTAS")
        print("1. Agregar venta")
        print("2. Mostrar ventas")
        print("3. Analizar ventas")
        print("4. Generar reporte PDF")
        print("5. Ver grafica de ventas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion =="1":
           registrar_venta()
    
        elif opcion =="2":
           ver_ventas()

        elif opcion =="3":
            analizar_ventas()

        elif opcion =="4":
            ventas = obtener_ventas()
            analisis = calcular_analisis_ventas()
            generar_grafica_ventas(analisis)
            generar_reporte_pdf(ventas, analisis)

            
        elif opcion =="5":
            print("generando grafica...")
            analisis= calcular_analisis_ventas()
            generar_grafica_ventas(analisis)

        elif opcion =="6":
           print("Hasta luego...")
           break
    
        else:
           print("Opcion no valida")



if __name__=="__main__":
    menu()
    
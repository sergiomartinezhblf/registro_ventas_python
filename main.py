from gestor_ventas import registrar_venta,ver_ventas,analizar_ventas


def menu():
    while True:
        print("===SISTEMA DE REGISTRO DE VENTAS")
        print("1. Agregar venta")
        print("2. Mostrar ventas")
        print("3. Analizar ventas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion =="1":
           registrar_venta()
    
        elif opcion =="2":
           ver_ventas()

        elif opcion =="3":
            analizar_ventas()
    
        elif opcion =="4":
           print("Hasta luego...")
           break
    
        else:
           print("Opcion no valida")



if __name__=="__main__":
    menu()

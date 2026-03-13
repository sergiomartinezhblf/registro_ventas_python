import matplotlib.pyplot as plt 

def generar_grafica_ventas(analisis):
    """
    Genera una gráfica de barras con:
    eje X -->productos
    eje Y -->total de dinero vendido
    """
    productos = []
    totales = []

    #ignorar el encabezado
    for fila in analisis[1:]:
        producto = fila[0]
        total = fila[2]

        productos.append(producto)
        totales.append(total)

    barras = plt.bar(productos,totales)
    plt.title("Ventas por Producto")
    plt.xlabel("Productos")
    plt.ylabel("Total de dinero")

    #agregar valores encima de cada barra
    for barra in barras:
        altura = barra.get_height()

        plt.text(
            barra.get_x()+barra.get_width()/2,
            altura,
            f"${altura:.2f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig("grafica_ventas.png")

    plt.close()

    print("Grafica guardada como grafica_ventas.png")




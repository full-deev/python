opcion = 6
#Datos de prueba para agilizar un poco el proceso
productos =[{'id': 100, 'nombre': 'paleta', 'precio': 10.0, 'stock': 15},
            {'id': 101, 'nombre': 'pepas', 'precio': 10.0, 'stock': 15},
            {'id': 102, 'nombre': 'papas', 'precio': 20.0, 'stock': 26},
            {'id': 103, 'nombre': 'arroz', 'precio': 65.0, 'stock': 99},
            {'id': 104, 'nombre': 'frutas', 'precio': 25.0, 'stock': 50},
            {'id': 105, 'nombre': 'bebids', 'precio': 16.0, 'stock': 33}]
def salir(a):
    if opcion == 0:
        print("\t*Gracias por usar nuestros servicios. ")
        exit()
def agregar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    for i in set (productos):
        if id_producto in productos[i]:
            print(f"\t**El ID {id_producto} ya está resgitrado. Ingrese otro ID")
            productos.pop(i)
            break
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Stock no válidp, ingrese nuevo: "))        
        productos.append({'id':ide,'nombre':nombre,'precio':precio,'stock':stock})            
def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    for i in range(len(productos)):
        if id_producto == productos[i]['id']:
            productos.pop(i)
            break
        else:
            print(f"El producto {id_producto} no existe.")
            break
def buscar_producto():
    id_producto = int(input("Ingresa el ID del producto: "))
    for i in range(len(productos)):           
        if id_producto != productos[i]['id']:
            continue
        else:
            print("Datos Encontrados\n","\nProducto: ",productos[i]['nombre'],"\nPrecio: $",productos[i]['precio'],"\nStock: ", productos[i]['stock'])
            break
def modificar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    for i in range(len(productos)):
        if id_producto == productos[i]['id']:
            nombre_producto = input("Ingrese el nuevo nombre del producto: ")
            precio_producto = float(input("Ingrese el nuevo precio del producto: "))
            stock_producto = int(input("Ingrese el nuevo stock del producto: "))
            productos[i]["nombre"] = nombre_producto
            productos[i]["precio"] = precio_producto
            productos[i]["stock"] = stock_producto
            break
        else:
            continue
def vender_producto():
    ver_stock()
    id_producto = int(input("Ingrese el ID del producto a vender: "))
    cantidad = int(input("Ingrese la cantidad a vender: "))
    for i in range(len(productos)):
        if productos[i]['id'] == id_producto:
            if productos[i]['stock'] >= cantidad:
                productos[i]['stock'] -= cantidad
                print(f"Venta exitosa.\n--DETALLES--\nProducto: ",productos[i]['nombre'],"\nPrecio: ", productos[i]['precio'],"\nCantidad: ",cantidad, "Total: ", productos[i]['precio'] * cantidad)
                break
            else:
                print("No hay suficiente stock del producto:", productos[i]["nombre"])
        else:
            continue
def ver_stock():
    for producto in productos:
        print(f"ID: {producto['id']} - Nombre: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['stock']}")
while opcion != 0:
    print("\n"  "   +---------------------------+\n"
                "   |    BIENVENIDOS A          |\n"
                "   |                           |\n" 
                "   |        LA TIENDA          |\n"
                "   |                           |\n"
                "   |            MILO ♦         |\n"
                "   +---------------------------+\n")
    print(            
        "    0 -> Salir\n"
        "    1 -> Agregar Productos\n"
        "    2 -> Eliminar Productos\n"
        "    3 -> Consultar Producto\n"
        "    4 -> Modificar Stock \n"
        "    5 -> Realizar una Venta\n"
        "    6 -> Mostrar inventario\n")    
    try:
        opcion = int((input("Ingresa el número de la opcion a consultar: ")))
        #Estoy agregando productos
        if opcion == 1: 
            print("\n---Menu Agregar Productos---"), agregar_producto()
        #Estoy eliminando productos
        elif opcion == 2:
            print("\n---Menu Eliminar Productos---"), eliminar_producto()
        #Consultar productos
        elif opcion == 3:
            print("\n---Consultar productos---"), buscar_producto()
        #Estoy modificando los productos
        elif opcion == 4:        
            print("\n---Menu Modificar Stock---"), modificar_producto()
        #Realizar una venta
        elif opcion == 5:
            print("\n---Venta de productos---"), vender_producto()
        #Vamos a mostrar el inventario
        elif opcion == 6:
            print("\n---Menu Inventario---"), ver_stock()
        elif opcion>6:
            print("\t**Valor fuera del rango permitido.")
        salir(0)
    except ValueError as ve:
        print(f"Ingrese solo números, Error! {ve} ")
opcion = " "
'''Datos de prueba para agilizar un poco el proceso'''
productos =[{'id': 100, 'nombre': 'paleta', 'precio': 10, 'stock': 15},
            {'id': 101, 'nombre': 'pepas', 'precio': 10, 'stock': 15},
            {'id': 102, 'nombre': 'papas', 'precio': 20, 'stock': 26},
            {'id': 103, 'nombre': 'arroz', 'precio': 65, 'stock': 99},
            {'id': 104, 'nombre': 'frutas', 'precio': 25, 'stock': 50}]
def salir(a):
    if opcion == 0:
        print("\t*Gracias por usar nuestros servicios. ")
        exit()

def agregar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    for i in range(len(productos)):           
        if id_producto == productos[i]['id']:
            print(f"\t**El ID {id_producto} ya está resgitrado. Ingrese otro ID")
            break
        else:
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = int(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto: "))
            productos.append({"id": id_producto, "nombre": nombre_producto, "precio": precio_producto, "stock": stock_producto})
            print(f"\t**Producto agregado {nombre_producto}")
            break

def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    for i in range(len(productos)):
        if id_producto == productos[i]['id']:
            productos.pop(i)
            break6
        else:
            print(f"El producto {id_producto} no existe.")
            break

def consultar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    


def modificar_producto():
    id_producto = int(input("Ingrese el ID del producto: "))
    if id_producto in productos:
        nombre_producto = input("Ingrese el nuevo nombre del producto: ")
        precio_producto = float(input("Ingrese el nuevo precio del producto: "))
        stock_producto = int(input("Ingrese el nuevo stock del producto: "))
        productos[id_producto]["nombre"] = nombre_producto
        productos[id_producto]["precio"] = precio_producto
        productos[id_producto]["stock"] = stock_producto
    else:
        print("El producto no existe.")

def vender_producto():
    id_producto = int(input("Ingrese el ID del producto a vender: "))
    cantidad = int(input("Ingrese la cantidad a vender: "))
    for producto in productos:
        if producto["id"] == id_producto:
            if producto["stock"] >= cantidad:
                producto["stock"] -= cantidad
                print("Se ha vendido el producto:", producto["nombre"])
        else:
            print("No hay suficiente stock del producto:", producto["nombre"])
        break

def ver_stock():
    for producto in productos:
        print(f"ID: {producto['id']} - Nombre: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['stock']}")


while opcion != 0:
    print("\n"  "   +---------------------------+\n"
                "   |    BIENVENIDOS A          |\n"
                "   |                           |\n" 
                "   |        LA TIENDA          |\n"
                "   |                           |\n"
                "   |            ABC ♦          |\n"
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
        #print(productos)
        opcion = int((input("Ingresa el número de la opcion a consultar: ")))
        #Estoy agregando productos'''          
        if opcion == 1: 
            print("\n****Menu Agregar Productos****\n")
            agregar_producto()
        #Estoy eliminando productos'''
        elif opcion == 2:
            print("\n****Menu Eliminar Productos**** \n")
            eliminar_producto()
        #Consultar productos
        elif opcion == 3:
            print("\n****Menu Consultar Productos**** \n")
            ide = int(input("Ingrese el ID: "))
            for i in range(len(productos)):           
                if ide != productos[i]['id']:                
                    #print("El ID no tiene registros asociados.")
                    continue
                else:
                    print("Datos Encontrados\n", 
                        "\nProducto: ", productos[i]['nombre']
                        ,"\nPrecio: ",productos[i]['precio']
                        ,"\nStock: ", productos[i]['stock']) 
                    break       
        #Estoy modificando los productos'''
        elif opcion == 4:        
            print("\n****Menu Modificar Stock**** \n")
            modificar_producto()
        #Realizar una venta
        elif opcion == 5:
            print("****Articulos Disponibles****\n")
            for i in range(len(productos)):
                print(f"ID-",productos[i]['id'], productos[i]['nombre'],"en stock:",productos[i]['stock'])
            ide = int(input("Ingrese el ID: "))
            ide = idFind(ide)        
            for i in range(len(productos)):
                if ide == productos[i]['id']:
                    cant = int(input("Ingresa la cantidad a vender: "))
                    if cant > 0 and cant < productos[i]['stock']:
                        nombre = productos[i]['nombre']
                        precio = productos[i]['precio']
                        stock = productos[i]['stock']
                        stock = stock - cant
                        tventa = precio * cant
                        productos.pop(i)
                        print("Venta en proceso !! ♦\n")
                        print(f"Su compra de {nombre} con numero de unidades: {cant} es un total de $ {tventa} \n")
                        productos.append({'id': ide,'nombre':nombre,'precio':precio,'stock':stock})
                    else:
                        print("Revise los datos ingresados y vuelva a ingresar.")                    
                else:
                    continue
            '''Vamos a mostrar inventario'''
        elif opcion == 6:
            ver_stock()

        salir(0)
    except ValueError as ve:
        print(f"Ingrese solo números, Error! {ve} ")
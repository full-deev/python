opcion = " "
'''Datos de prueba para agilizar un poco el proceso'''
productos =[{'id': 101, 'nombre': 'ppas', 'precio': 10, 'stock': 15}, 
          {'id': 102, 'nombre': 'papas', 'precio': 20, 'stock': 26}, 
          {'id': 103, 'nombre': 'arroz', 'precio': 65, 'stock': 99}, 
          {'id': 104, 'nombre': 'frutas', 'precio': 25, 'stock': 50},
          {'id': 105, 'nombre': 'harina', 'precio': 15, 'stock': 50},
          {'id': 106, 'nombre': 'huevos', 'precio': 88, 'stock': 13}]
while opcion != 0:
    print("")
    print(      "   +---------------------------+\n"
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
        "    6 -> Mostrar inventario\n"
        )
    opcion = int((input("Ingresa el numero de la opcion a consultar: ")))
    '''Estoy agregando productos'''
    if opcion == 1:
        print("\n****Menu Agregar Productos****\n")
        ide = int(input("Ingrese el ID: "))
        if ide < 0:
                ide = int(input("Revisa ID e ingresa nuevamente: "))
        for i in range(len(productos)):
            if ide == productos[i]['id']:
                print(("Ya existe, es necesario una actualización..."))
                productos.pop(i)
                break
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio: "))
        if precio < 0:
            precio = int(input("Corrija el precio e ingrese: "))
        stock = int(input("Ingrese la cantidad en stock: "))
        if stock < 0:
            stock = int(input("Stock no válidp, ingrese nuevo: "))        
        productos.append({'id':ide,'nombre':nombre,
                        'precio':precio,'stock':stock})
        '''Estoy eliminando productos'''
    elif opcion == 2:
        print("\n****Menu Eliminar Productos**** \n")
        ide = int(input("Ingrese el ID del producto a eliminar: "))
        if ide < 0:
                ide = int(input("Revisa ID e ingresa nuevamente: "))                    
        for i in range(len(productos)):
            if ide == productos[i]['id']:
                productos.pop(i)
                break
            else:
                print("Producto no encontrado, agreguelo para así poder eliminarlo.")
        '''Estoy buscando productos'''
    elif opcion == 3:
        print("\n****Menu Consultar Productos**** \n")
        ide = int(input("Ingrese el ID a consultar "))
        if ide < 0:
            ide = int(input("Revisa ID e ingresa nuevamente: "))
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
        '''Estoy modificando los productos'''
    elif opcion == 4:        
        print("\n****Menu Modificar Stock**** \n")
        ide = int(input("Ingrese el ID a consultar "))
        if ide < 0:
            ide = int(input("Revisa ID e ingresa nuevamente: "))
        for i in range(len(productos)):
            if ide == productos[i]['id']:
                print("Stock actual", productos[i]['stock'])
                stock = int(input("Ingrese el nuevo stock: "))
                if stock < 0:
                    stock = int(input("Stock no válido, ingrese nuevo: "))
                    nombre = productos[i]['nombre']
                    precio = productos[i]['precio']              
                    productos.pop(i)                                 
                    productos.append({'id':ide,'nombre':nombre,'precio':precio,'stock':stock})
                    break
                else:
                    nombre = productos[i]['nombre']
                    precio = productos[i]['precio']              
                    productos.pop(i)                                 
                    productos.append({'id':ide,'nombre':nombre,'precio':precio,'stock':stock})
                    break
    elif opcion == 5:
        print("****Articulos Disponibles****\n")
        for i in range(len(productos)):
            print(f"ID-",productos[i]['id'], productos[i]['nombre'],"en stock:",productos[i]['stock'])
        ide = int(input("\nIngrese el ID a vender: "))
        if ide < 0:
            ide = int(input("Revisa ID e ingresa nuevamente: "))        
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
        print("\n****Menu Inventario**** \n")
        print("INVENTARIO TIENDA ABC ♦\n")
        print("ID","NOM","CASH","CANT", sep=" | ", end=" |\n")
        for i in range(len(productos)):
            idd = productos[i]['id']
            name = productos[i]['nombre']
            price = productos[i]['precio']
            size = productos[i]['stock']            
            print(idd, name, price, size, sep=" | ", end=" | \n")
    else:
        if opcion == 0:print("\nHasta luego, vuelva pronto... ♥")
        else: print("Digitos, no válidos, corrijalos !!")
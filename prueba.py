opcion = " "
productos =[{'id': 101, 'nombre': 'ppas', 'precio': 10, 'stock': 15}, 
          {'id': 102, 'nombre': 'papas', 'precio': 20, 'stock': 26}, 
          {'id': 103, 'nombre': 'arroz', 'precio': 65, 'stock': 99}, 
          {'id': 104, 'nombre': 'frutas', 'precio': 25, 'stock': 50},
          {'id': 105, 'nombre': 'harina', 'precio': 15, 'stock': 50},
          {'id': 106, 'nombre': 'gelatinas', 'precio': 88, 'stock': 13}]
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
    print(productos)
    '''Estoy agregando productos'''
    if opcion == 1:
        print("\n****Menu Agregar Productos****\n")
        ide = int(input("Ingrese el ID: "))
        if ide < 0:
                ide = int(input("Revisa ID e ingresa nuevamente: "))
        for i in range(len(productos)):
            if ide == productos[i]['id']:
                print(("Ya existe, vamos actualizarlo..."))
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
        print(f"agregar  {productos}\n")
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
        print(f"\n eliminar y actualizadoo \n  {productos}")
        '''Estoy buscando productos'''
    elif opcion == 3:
        print("\n****Menu Consultar Productos**** \n")
        ide = int(input("Ingrese el ID a consultar "))
        if ide < 0:
            ide = int(input("Revisa ID e ingresa nuevamente: "))
        for i in range(len(productos)):           
            if ide != productos[i]['id']:                
                print("El ID no tiene registros asociados.")
                continue
            else:
                print("Datos Encontrados\n", 
                      "\nProducto: ", productos[i]['nombre']
                      ,"\nPrecio: ",productos[i]['precio']
                      ,"\nStock: ", productos[i]['stock']) 
                break       
        print(f"\n consultar{productos}")
        '''Estoy modificando los productos'''
    elif opcion == 4:        
        print("\n****Menu Modificar Stock**** \n")
        ide = int(input("Ingrese el ID a consultar "))
        if ide < 0:
            ide = int(input("Revisa ID e ingresa nuevamente: "))     
        for i in range(len(productos)):
            if ide == productos[i]['id']:
                print("Stock actual ", productos[i]['stock'])
                nombre = productos[i]['nombre']
                precio = productos[i]['precio']
                break
        stock = int(input("Ingrese el nuevo stock: "))
        if stock < 0:
            stock = int(input("Stock no válido, ingrese nuevo: "))                     
        productos.append({'id':ide,'nombre':nombre,
                        'precio':precio,'stock':stock})            
        print(f"\n modificar  {productos}")

        '''Estoy vendiendo productos'''
    elif opcion == 5:
        print("\n****Menu Vender****")
        for i in range(len(productos)):
            print(f"\n ID-",productos[i]['id'], productos[i]['nombre'],"en stock:",productos[i]['stock'])
        ide = int(input("Ingrese el ID a vender: "))
        if ide < 0:
            ide = int(input("Revisa ID e ingresa nuevamente: "))        
        for j in range(len(productos)):
            if ide == productos[j]['id']:
                buy = int(input("Ingresa la cantidad a vender: "))
                if buy < 0:
                    buy = int(input("Cantidad ingresada no valida, ingrese otra: "))
                    if buy > productos[j]['stock']:
                        print("Cantidad a comprar no puede ser mayor a la mostrada en pantalla")
                    else:
                        res = ((productos[j][stock]) - (buy))     
                        print(res)  
            else:
                continue
                print(f"{ide}, no encontrado")

        '''Vamos a mostrar inventario'''
    elif opcion == 6:
        print("\n****Menu Inventario**** \n")
        print("TIENDA ABC ♣")
        print("INVENTARIO TIENDA ABC ♦\n")
        print("ID","NOM","CASH","CANT", sep=" | ", end=" |\n")
        for i in range(len(productos)):
            idd = productos[i]['id']
            name = productos[i]['nombre']
            price = productos[i]['precio']
            size = productos[i]['stock']            
            print(idd, name, price, size, sep=" | ", end=" | \n")
            #print("ID {} - PRODUCTO {} PRECIO {} CANTIDAD {}".format(idd, name, price, size))

        #print (productos)
    else:
        if opcion == 0:print("\nHasta luego, vuelva pronto... ♥")
        else: print("Digitos, no válidos, corrijalos !!")
opcion = " "
lis_pro =[]
while opcion != 0:
    print("")
    print(      "|---------------------------|\n"
                "|    BIENVENIDOS A          |\n"
                "|                           |\n"
                "|        LA TIENDA          |\n"
                "|                           |\n"
                "|            UTE ☻          |\n"
                "|---------------------------|\n")
    print(            
        "    0 -> Salir\n"
        "    1 -> Agregar Productos\n"
        "    2 -> Eliminar Productos\n"
        "    3 -> Consultar Producto\n"
        "    4 -> Modificar Stock \n")

    opcion = int(input("Ingresa el numero de la opcion a consultar: "))
    if opcion == 1:
        print("****Menu Agregar Productos")
        ide = int(input("Ingrese el ID "))
        nombre = input("Ingrese el nombre del producto ")
        precio = input("Ingrese el precio ")
        stock = input("Ingrese la cantidad en stock ")
        lis_pro.append({'id':ide,'nombre':nombre, 'precio':precio, 'stock':stock})

    elif opcion == 2:
        print("****Menu Eliminar Productos")

    elif opcion == 3:
        print("****Menu Consultar Productos")
        idd = int(input("Ingrese el ID a consultar "))
        for i in lis_pro:
            if idd == i['id']:
                print("Producto encontrado")
            else:
                print("El ID consultado no existe. ")

    elif opcion == 4:
        print("****Menu Modificar Stock")
        
    else:
        if opcion == 0:
            print("Hasta luego, vuelva pronto...")
        else:
            print ("Usted a ingresado una opcion no válida")
    
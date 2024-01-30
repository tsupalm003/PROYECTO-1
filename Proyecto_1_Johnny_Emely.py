# PROYECTO 1
# INTEGRANTES: JOHNNY BRICEÑO, EMELY YOVERA

# Sistema de Administración de Inventario para una Ferretería

print("------------------------------------------------------------")
print("Sistema de Administración de Inventario para una Ferretería")
print("------------------------------------------------------------")

# Lista para almacenar los productos en el inventario
inventario = []

# Bucle principal del programa
while True:
    # Menú de opciones
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Eliminar producto")
    print("4. Buscar producto")
    print("5. Actualizar cantidad y precio de un producto")
    print("6. Mostrar lista de productos")
    print("7. Salir")

    # Solicitar al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Opción 1: Agregar producto
    if opcion == "1":
        # Solicitar información del nuevo producto
        nombre = input("Ingrese el nombre del producto: ")

        # Verificar si el producto ya existe en el inventario
        producto_existente = False
        for producto in inventario:
            if producto['nombre'] == nombre:
                producto_existente = True
                break

        # El programa indica que el producto ya esta en el inventario
        if producto_existente:
            print(f"El producto {nombre} ya existe en el inventario.")
            # Procesar la información del nuevo producto
        else:
            categoria = input("Ingrese la categoría del producto: ")
            stock = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio del producto: "))

            # Crear un diccionario para representar el nuevo producto
            nuevo_producto = {
                'nombre': nombre,
                'categoria': categoria,
                'stock': stock,
                'precio': precio
            }

            # Agregar el nuevo producto al inventario
            inventario.append(nuevo_producto)
            print(f"Producto {nombre} agregado al inventario.")

    # Opción 2: Mostrar inventario
    elif opcion == "2":
        print("Inventario:")
        # Iterar a través de los productos en el inventario y mostrar la información
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Stock: {producto['stock']}")
            print(f"Precio: ${producto['precio']}")
            print("-----------------------")

    # Opción 3: Eliminar producto
    elif opcion == "3":
        # Solicitar el nombre del producto a eliminar
        nombre = input("Ingrese el nombre del producto a eliminar: ")

        # Buscar el producto en el inventario y eliminarlo
        for producto in inventario:
            if producto['nombre'] == nombre:
                inventario.remove(producto)
                print(f"Producto {nombre} eliminado del inventario.")
                break
        else:
            print(f"El producto {nombre} no fue encontrado en el inventario.")

    # Opción 4: Buscar producto
    elif opcion == "4":
        # Solicitar el nombre o categoría para buscar
        criterio = input("Ingrese el nombre o categoría a buscar: ")

        # Buscar productos que coincidan con el criterio de búsqueda
        encontrados = []
        for producto in inventario:
            if criterio.lower() in producto['nombre'].lower() or criterio.lower() in producto['categoria'].lower():
                encontrados.append(producto)

        # Mostrar resultados de la búsqueda
        if encontrados:
            print("Resultados de la búsqueda:")
            for producto in encontrados:
                print(f"Nombre: {producto['nombre']}")
                print(f"Categoría: {producto['categoria']}")
                print(f"Stock: {producto['stock']}")
                print(f"Precio: ${producto['precio']}")
                print("-----------------------")
        else:
            print("No se encontraron productos con el criterio de búsqueda.")

    # Opción 5: Actualizar cantidad y precio de un producto
    elif opcion == "5":
        # Solicitar el nombre del producto a actualizar
        nombre = input("Ingrese el nombre del producto a actualizar: ")

        # Buscar el producto en el inventario y actualizar la información
        for producto in inventario:
            if producto['nombre'] == nombre:
                nuevo_stock = int(input("Ingrese la nueva cantidad en stock: "))
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))

                # Actualizar la cantidad y el precio del producto
                producto['stock'] = nuevo_stock
                producto['precio'] = nuevo_precio

                print(f"Cantidad y precio de {nombre} actualizados en el inventario.")
                break
        else:
            print(f"El producto {nombre} no fue encontrado en el inventario.")

    # Opción 6: Mostrar lista de productos
    elif opcion == "6":
        print("Lista de productos:")
        # Mostrar información resumida de cada producto en el inventario
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, Stock: {producto['stock']}, Precio: ${producto['precio']}")

    # Opción 7: Salir
    elif opcion == "7":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # Manejo de opciones no válidas
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

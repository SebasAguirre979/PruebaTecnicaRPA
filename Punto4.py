def mostrar_menu():
    print("-" * 50)
    print("Sistema de inventario. Ingrese una opcion:")
    print("1. Agregar producto")
    print("2. Ver reporte inventario")
    print("3. Salir\n")

def sub_menu():
    print("-" * 50)
    print("Que grupo desear ver:")
    print("1. Dairy")
    print("2. Cleaning")
    print("3. Grain")
    print("4. Salir\n")

def menu_grupo():
    print("-" * 50)
    print("En que grupo se guardara el producto:")
    print("1. Dairy")
    print("2. Cleaning")
    print("3. Grain")
    print("4. Salir\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Opción 1.\n")
            print("Datos del producto a guardar.")
            nombre = input("Ingrese el nombre: ")
            cantidad = input("Ingrese la cantidad: ")

            if cantidad.isdigit():
                menu_grupo()
                opcion_grupo = input("Seleccione una opción: ")
                if opcion_grupo == "1":
                    guardar_producto(dairy_products, dairy_stock, nombre, cantidad)
                elif opcion_grupo == "2":
                    guardar_producto(cleaning_products, cleaning_stock, nombre, cantidad)
                elif opcion_grupo == "3":
                    guardar_producto(grain_products, grain_stock, nombre, cantidad)
                elif opcion == "4":
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida. Seleccione una opción válida.")
            else:
                print("--CANTIDAD INGRESADA INVALIDA--\n")
            
        elif opcion == "2":
            sub_menu()
            opcion_sub = input("Seleccione una opción: ")
            if opcion_sub == "1":
                print("Opción 1.\n")
                print("{:<25} {:<25}".format("Nombre", "Inventario"))
                print("-" * 40)
                ver_inventario(dairy_products, dairy_stock)
                print("-" * 40)
            elif opcion_sub == "2":
                print("Opción 2.\n")
                print("{:<25} {:<25}".format("Nombre", "Inventario"))
                print("-" * 40)
                ver_inventario(cleaning_products, cleaning_stock)
                print("-" * 40)
            elif opcion_sub == "3":
                print("Opción 3.\n")
                print("{:<25} {:<25}".format("Nombre", "Inventario"))
                print("-" * 40)
                ver_inventario(grain_products, grain_stock)
                print("-" * 40)
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Seleccione una opción válida.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Seleccione una opción válida.")

def ver_inventario(arreglo_productos, arreglo_stock):
    for elemento1, elemento2 in zip(arreglo_productos, arreglo_stock):
        print("{:<25} {:<25}".format(str(elemento1), str(elemento2)))

def guardar_producto(arreglo_prod, arreglo_stoc, nombre, cantidad):
    for indice, elemento in enumerate(arreglo_prod):
        if elemento == nombre:
            arreglo_stoc[indice] += int(cantidad)
            print("--PRODUCTO EXISTENTE, INVENTARIO ACTUALIZADO--\n")
            return
    arreglo_prod.append(nombre)
    arreglo_stoc.append(cantidad)
    print("--PRODUCTO AGREGADO--\n")

dairy_products = ["“Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]

cleaning_products = ["Detergent", "Dishwashing liquid", "Air freshener"]
cleaning_stock = [44, 10, 25]

grain_products = ["Pasta", "Bread", "Breakfast cereals", "Grits"]
grain_stock = [10, 55, 6, 25]

main()
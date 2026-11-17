from busqueda import buscar_libro


def mostrar_menu():
    print("\n=== MINI BIBLIOTECA ===")
    print("3. Buscar libro")
    print("0. Salir")


def main():
    biblioteca = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("¡Hasta pronto!")
            break
        elif opcion == "3":
            buscar_libro(biblioteca)
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
import libros

def mostrar_menu():
    print("\n=== MINI BIBLIOTECA ===")
    print("1. Añadir libro")
    print("2. Listar libros")
    print("0. Salir")
def main():
    biblioteca = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        elif opcion == "1":
            biblioteca = libros.anadir_libro(biblioteca)
            break
        elif opcion == "2":
            libros.listar_libros(biblioteca)
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
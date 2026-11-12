def anadir_libro(biblioteca):
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    year = int(input("Introduce el año del libro: "))
    
    libro = {"titulo": titulo,"autor": autor,"year": year}
    biblioteca.append(libro)
    return biblioteca

def listar_libros(biblioteca):
    if len(biblioteca) > 0:
        for i, libro in enumerate(biblioteca, 1):
            print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['year']})")
    else:
        print("No hay libros disponibles")

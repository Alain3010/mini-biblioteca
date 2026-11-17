ARCHIVO = "libros.txt"


def guardar_libros(biblioteca):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for libro in biblioteca:
            f.write(f"{libro['titulo']};{libro['autor']};{libro['year']}\n")
    print(f"Se han guardado {len(biblioteca)} libros en {ARCHIVO}")


def cargar_libros():
    biblioteca = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    titulo, autor, year = linea.split(";")
                    biblioteca.append({"titulo": titulo, "autor": autor, "year": int(year)})
    except FileNotFoundError:
        pass
    return biblioteca

def buscar_libro(biblioteca:list):
    results =[]
    busqueda = input("introduce tu busqueda: ").lower()
    for libro in biblioteca:
        if busqueda in libro["titulo"].lower() or busqueda in libro["autor"].lower():       
            results.append(libro)
    return results

libros = []

def agregar_libro(titulo, autor, isbn):
    if any(libro['isbn'] == isbn for libro in libros):
        raise ValueError("El ISBN ya existe")
    libros.append({"titulo": titulo, "autor": autor, "isbn": isbn})

def eliminar_libro(isbn):
    global libros
    libros = [libro for libro in libros if libro['isbn'] != isbn]

def buscar_libro(titulo):
    return [libro for libro in libros if titulo.lower() in libro['titulo'].lower()]

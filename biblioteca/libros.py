import os
DATA_FILE = "LIBROS.txt"
libros=[]

def agregar_libro(titulo, autor, isbn):
    try:
        if any(libro['isbn'] == isbn for libro in libros):
            raise ValueError("El ISBN ya existe")
        with open(DATA_FILE, "a") as file:
            file.write(f"{titulo}, {autor}, {isbn}\n")
    except FileNotFoundError:
        print(f"Error: El archivo {file} no fue encontrado")

def leer_libro():
    if not os.path.exists(DATA_FILE):
        return []

    libros = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            titulo, autor, isbn = line.strip().split(", ")
            libros.append((titulo, autor, isbn))
        return libros

def leer_libro_():
    if not os.path.exists(DATA_FILE):
        return []

    libros = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            titulo, autor, isbn = line.strip().split(", ")
            libros.append((isbn, titulo, autor))
        return libros

def leer_libro_prestado():
    if not os.path.exists("LIBROS_PRESTADOS.txt"):
        return []

    libros = []
    with open("LIBROS_PRESTADOS.txt", "r") as file:
        for line in file:
            titulo, autor, isbn = line.strip().split(", ")
            libros.append((titulo, autor, isbn))
        return libros

def listar_libros():
    libros = leer_libro()
    return libros

def listar_libros_():
    libros = leer_libro_()
    return libros

def guardar_libro(libros):
    with open(DATA_FILE, "w+") as file:
        for libro in libros:
            file.write(", ".join(libro) + "\n")

def eliminar_libro(isbn):
    librs = leer_libro()
    listar_libros()
    isbn = isbn.split(" - ")
    isbn = isbn[0]
    if isbn != "":
        for l in librs:
            if isbn == l[2]:
                librs.pop(librs.index(l))
        guardar_libro(librs)
        print("Producto eliminado exitosamente.")
    else:
        print("Numero invalido")

def eliminar_libro_prestado(isbn):
    librs = leer_libro_prestado()
    isbn = isbn.split(" - ")
    isbn = isbn[0]
    if isbn != "":
        for l in librs:
            if isbn == l[2]:
                librs.pop(librs.index(l))
        guardar_libro(librs)
        print("Producto eliminado exitosamente.")
    else:
        print("Numero invalido")

def buscar_libro(titulo):
    libros = leer_libro()
    return [libro for libro in libros if titulo.lower() in libro[0].lower()]

def buscar_libro_por_isbn(isbn):
    isbn = isbn.split(" - ")
    libros = leer_libro()
    return [libro for libro in libros if isbn[0].lower() in libro[2].lower()]

def buscar_libro_prestado_por_isbn(isbn):
    isbn = isbn.split(" - ")
    print(isbn)
    libros = leer_libro_prestado()
    print(libros)
    return [libro for libro in libros if isbn[0].lower() in libro[2].lower()]

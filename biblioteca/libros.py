import os
DATA_FILE = "LIBROS.txt"
libros=[]

def agregar_libro(titulo, autor, isbn):
    try:
        if any(libro['isbn'] == isbn for libro in libros):
            raise ValueError("El ISBN ya existe")
        with open(DATA_FILE, "a") as file:
            file.write(f"{isbn}, {titulo}, {autor}\n")
    except FileNotFoundError:
        print(f"Error: El archivo {file} no fue encontrado")

def leer_libro():
    if not os.path.exists(DATA_FILE):
        return []

    libros = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            isbn, titulo, autor = line.strip().split(", ")
            libros.append(f"{isbn} - {titulo} - {autor}\n")
        return libros

def leer_libro_():
    if not os.path.exists(DATA_FILE):
        return []

    libros = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            isbn, titulo, autor = line.strip().split(", ")
            libros.append((isbn + " - " + titulo + " - " + autor))
        return libros

def leer_libro_prestado():
    if not os.path.exists("LIBROS_PRESTADOS.txt"):
        return []

    libros = []
    with open("LIBROS_PRESTADOS.txt", "r") as file:
        for line in file:
            isbn, titulo, autor = line.strip().split(", ")
            libros.append((isbn + " - " + titulo + " - " + autor))
        return libros

def leer_libro_prestado_():
    if not os.path.exists("LIBROS_PRESTADOS.txt"):
        return []

    libros = []
    with open("LIBROS_PRESTADOS.txt", "r") as file:
        for line in file:
            isbn, titulo, autor = line.strip().split(", ")
            libros.append((isbn + " - " + titulo + " - " + autor))
            print((titulo, autor, isbn))
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
            file.write(f"{libro[0]}, {libro[1]}, {libro[2]}")

def guardar_libro_(libros):
    with open(DATA_FILE, "w+") as file:
        for libro in libros:
            libro = libro.split(" - ")
            file.write(f"{libro[0]}, {libro[1]}, {libro[2]}\n")

def eliminar_libro(isbn):
    librs = leer_libro()
    lista = []
    listar_libros()
    isbn = isbn.split(" - ")
    isbn = isbn[0]
    if isbn != "":
        for l in librs:
            indice = librs.index(l)
            l = l.split(" - ")
            if isbn == l[0]:
                librs.pop(indice)
            else:
                lista.append(l)
        guardar_libro(lista)
        print("Producto eliminado exitosamente.")
    else:
        print("Numero invalido")

def eliminar_libro_prestado(isbn):
    librs = leer_libro_prestado_()

    isbn = isbn[0]
    if isbn != "":
        for l in librs:
            l = l.split(" - ")
            if isbn == l[2]:
                librs.pop(l.index(l[0]))
        guardar_libro(librs)
        print("Producto eliminado exitosamente.")
    else:
        print("Numero invalido")

def buscar_libro(titulo):
    libros = leer_libro()
    lista=[]
    for l in libros:
        l = l.split(" - ")
        if titulo.lower() in l[1].lower():
            lista.append(l)
    return lista
    #return [libro for libro in libros if titulo.lower() in libro[1].lower()]

def buscar_libro_por_isbn(isbn):
    isbn = isbn.split(" - ")
    libros = leer_libro()
    for l in libros:
        l = l.split(" - ")
        if isbn[0] == l[0]:
            return l
    #return [libro for libro in libros if isbn[0].lower() in libro[2].lower()]

def buscar_libro_prestado_por_isbn(isbn):
    isbn = isbn.split(" - ")
    libros = leer_libro_prestado_()
    print(libros)
    return [libro for libro in libros if isbn.lower() in libro.lower()]

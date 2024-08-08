from biblioteca import libros
import os
prestamos = []
libros_prestados = []
DATA_FILE = "PRESTAMOS.txt"

def prestar_libro(isbn, id_usuario):
    try:
        libroE = libros.buscar_libro_por_isbn(isbn)
        agregar_libros_prestados(libroE)
        libros.eliminar_libro(isbn)

        if libroE:
            with open(DATA_FILE, "a") as file:
                file.write(f"El usuario: {id_usuario} ISBN: {isbn}, \n")
        prestamos.append({"isbn": isbn, "id_usuario": id_usuario})
    except FileNotFoundError:
        print(f"Error: El archivo {file} no fue encontrado")

def devolver_libro(isbn):
    libros_prestados = leer_libros_prestados()
    for libro in libros_prestados:
        if libro[2] == isbn[0]:
            libros.eliminar_libro_prestado(isbn)

def agregar_libros_prestados(libro):
    libro = libro[0]
    with open("LIBROS_PRESTADOS.txt", "a") as file:
        file.write(f"{libro[0]}, {libro[1]}, {libro[2]}\n")
    libros_prestados.append(f"{libro[0]}, {libro[1]}, {libro[2]}")

def leer_prestamos():
    if not os.path.exists(DATA_FILE):
        return []
    libros = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            isbn, id_usuario = line.strip().split(", ")
            libros.append(isbn + " - " + id_usuario)
        return libros

def leer_libros_prestados():
    if not os.path.exists("LIBROS_PRESTADOS.txt"):
        return []
    libros = []
    with open("LIBROS_PRESTADOS.txt", "r") as file:
        for line in file:
            nombre, autor, isbn = line.strip().split(", ")
            libros.append((nombre, autor, isbn))
        return libros

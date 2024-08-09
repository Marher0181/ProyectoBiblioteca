import datetime

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
                file.write(f"{id_usuario}, {isbn}, {datetime.date.today()} \n")
        prestamos.append(f"{id_usuario}, {isbn}")
    except FileNotFoundError:
        print(f"Error: El archivo {file} no fue encontrado")

def devolver_libro(isbn):
    libros_prestados = leer_libros_prestados()

    libroP = libros.buscar_libro_prestado_por_isbn(isbn)
    isbn = isbn.split(" - ")
    for libro in libros_prestados:
        if libro[2] == isbn[0]:
            libros.eliminar_libro_prestado(isbn)

def agregar_libros_prestados(libro):

    print(libro)
    with open("LIBROS_PRESTADOS.txt", "a") as file:
        file.write(f"{libro[0]}, {libro[1]}, {libro[2]}\n")
    libros_prestados.append(f"{libro}")

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
            libros.append((isbn + " - " + nombre + " - " + autor))
        return libros

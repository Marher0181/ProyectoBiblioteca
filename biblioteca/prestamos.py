from biblioteca import libros
import os
prestamos = []
libros_prestados = []
DATA_FILE = "PRESTAMOS.txt"

def prestar_libro(isbn, id_usuario):
    try:
        libroE = libros.buscar_libro_por_isbn(isbn)

        if libroE:
            libros.eliminar_libro(isbn)

            with open("prestamos.txt", "a") as prestamos_file:
                prestamos_file.write(f"{isbn},{id_usuario}\n")

            print(f"Libro con ISBN {isbn} prestado al usuario {id_usuario}.")
        else:
            print(f"Error: El libro con ISBN {isbn} no está disponible.")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")

def devolver_libro(isbn, id_usuario):
    try:
        with open("prestamos.txt", "r") as prestamos_file:
            prestamos = prestamos_file.readlines()

        with open("prestamos.txt", "w") as prestamos_file:
            for prestamo in prestamos:
                prestamo_isbn, prestamo_usuario = prestamo.strip().split(", ")
                if prestamo_isbn != isbn or prestamo_usuario != id_usuario:
                    prestamos_file.write(f"{prestamo}\n")

        with open("libros.txt", "a") as libros_file:
            libros_file.write(f"{isbn}\n")

        print(f"Libro con ISBN {isbn} devuelto por el usuario {id_usuario}.")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")


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

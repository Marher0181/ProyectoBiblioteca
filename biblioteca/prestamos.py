prestamos = []

def prestar_libro(isbn, id_usuario):
    if any(prestamo['isbn'] == isbn for prestamo in prestamos):
        raise ValueError("El libro ya está prestado")
    prestamos.append({"isbn": isbn, "id_usuario": id_usuario})

def devolver_libro(isbn, id_usuario):
    global prestamos
    prestamos = [prestamo for prestamo in prestamos if not (prestamo['isbn'] == isbn and prestamo['id_usuario'] == id_usuario)]

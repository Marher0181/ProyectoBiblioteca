morosos = []

def morosidad(isbn, id_usuario):
    return any(moroso['isbn'] == isbn and moroso['id_usuario'] == id_usuario for moroso in morosos)

def devolver_conmorosidad(isbn, id_usuario):
    if morosidad(isbn, id_usuario):
        # Aquí se puede agregar lógica adicional para la morosidad
        pass
    #devolver_libro(isbn, id_usuario)

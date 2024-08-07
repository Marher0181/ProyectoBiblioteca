morosos = []

def morosidad(isbn, id_usuario):
    return any(moroso['isbn'] == isbn and moroso['id_usuario'] == id_usuario for moroso in morosos)

def devolver_conmorosidad(isbn, id_usuario):
    if morosidad(isbn, id_usuario):
        pass

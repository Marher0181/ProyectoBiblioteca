usuarios = []

def registrar_usuario(nombre, id_usuario):
    if any(usuario['id_usuario'] == id_usuario for usuario in usuarios):
        raise ValueError("El ID de usuario ya existe")
    usuarios.append({"nombre": nombre, "id_usuario": id_usuario})

def eliminar_usuario(id_usuario):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id_usuario'] != id_usuario]

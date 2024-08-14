import random
import os
usuarios = []
DATA_FILE = "USUARIOS.txt"

def registrar_usuario(nombre):
    id_usuario = int(random.uniform(0, 1024))
    try:
        while any(usuario['id_usuario'] == id_usuario for usuario in usuarios):
            id_usuario = int(random.uniform(0, 1024))
        with open(DATA_FILE, "a") as file:
            file.write(f"{nombre}, {id_usuario}\n")
    except FileNotFoundError:
        print(f"Error: El archivo {file} no fue encontrado")


def eliminar_usuario(id_usuario):
    usuarios = leer_usuarios()
    listar_usuarios()
    if id_usuario != "":
        for l in usuarios:
            if id_usuario == l[1]:
                usuarios.pop(usuarios.index(l))
        guardar_usuarios(usuarios)

def guardar_usuarios(usuaris):
    with open(DATA_FILE, "w+") as file:
        for usuario in usuaris:
            file.write(", ".join(usuario) + "\n")

def guardar_usuarios_(usuaris):
    with open(DATA_FILE, "w+") as file:
        for usuario in usuaris:
            usuario = usuario.split(" - ")
            file.write(f"{usuario[0]}, {usuario[1]}\n")

def buscar_usuario(nombreU):
    return [nombre for nombre in usuarios if nombreU.lower() in nombre['titulo'].lower()]

def listar_usuarios():
    usuarios = leer_usuarios()
    return usuarios

def listar_usuarios_():
    usuarios = leer_usuarios_()
    return usuarios


def leer_usuarios():
    if not os.path.exists(DATA_FILE):
        return []

    usuarios = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            nombre, id_usuario = line.strip().split(", ")
            usuarios.append((nombre, id_usuario))
        return usuarios

def leer_usuarios_():
    if not os.path.exists(DATA_FILE):
        return []

    usuarios = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            id_usuario, nombre  = line.strip().split(", ")
            usuarios.append(id_usuario + " - " + nombre)
        return usuarios


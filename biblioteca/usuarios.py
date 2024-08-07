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
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id_usuario'] != id_usuario]

def buscar_usuario(nombreU):
    return [nombre for nombre in usuarios if nombreU.lower() in nombre['titulo'].lower()]

def listar_usuarios():
    usuarios = leer_usuarios()
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



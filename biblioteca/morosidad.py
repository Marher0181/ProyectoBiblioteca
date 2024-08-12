from datetime import datetime
from biblioteca import libros
import os
prestamos = []
libros_prestados = []
DATA_FILE = "PRESTAMOS.txt"

def leer_prestamos_p_morosidad():
    if not os.path.exists(DATA_FILE):
        return []
    prestamos = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            usuario, libro, fecha_prestamo = line.strip().split(", ")
            prestamos.append(f"{usuario}, {libro}, {fecha_prestamo}")
    return prestamos

def leer_prestamos_p_morosidad_rec():
    if not os.path.exists(DATA_FILE):
        return []
    prestamos = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            usuario, libro, fecha_prestamo = line.strip().split(", ")
            comparacion = fecha_prestamo.split("-")
            comparacionY = int(comparacion[0])
            comparacionM = int(comparacion[1])
            comparacion = int(comparacion[2])
            nuevo = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
            if nuevo <= datetime.today():
                if comparacionY > datetime.today().year and comparacionM > datetime.today().months:
                    if comparacionM > datetime.today().month and comparacionY > datetime.today().year:
                        prestamos.append(f"{usuario}, {libro}, {fecha_prestamo}, ESTÁ CON MORA SOBREPASÓ FECHA LIMITE POR {datetime.today().year - comparacionY} AÑOS y {datetime.today().month - comparacionM} MESES")
                        if comparacionM >= datetime.today().month:
                            prestamos.append(f"{usuario}, {libro}, {fecha_prestamo}, ESTÁ CON MORA SOBREPASÓ FECHA LIMITE por {datetime.today().month - comparacionM} Meses y {datetime.today().day - comparacion} DIAS")
                        else:
                            prestamos.append(f"{usuario}, {libro}, {fecha_prestamo}, falta poco para que sea fecha limite")
                else:
                    prestamos.append(
                        f"{usuario}, {libro}, {fecha_prestamo}, ESTÁ CON MORA SOBREPASÓ FECHA LIMITE POR {comparacionY - datetime.today().year} AÑOS")
            else:
                prestamos.append(f"{usuario}, {libro}, {fecha_prestamo}")
    return prestamos


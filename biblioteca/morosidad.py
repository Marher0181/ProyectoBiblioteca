from datetime import datetime, timedelta
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
    dias_de_mora = 15  # Definimos el límite de días para considerar mora

    with open(DATA_FILE, "r") as file:
        for line in file:
            usuario, libro, fecha_prestamo = line.strip().split(", ")
            fecha_prestamo_dt = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
            fecha_limite = fecha_prestamo_dt + timedelta(days=dias_de_mora)
            fecha_actual = datetime.today()

            if fecha_actual > fecha_limite:
                # Cálculo de diferencia entre la fecha actual y la fecha límite
                diferencia = fecha_actual - fecha_limite
                dias_retraso = diferencia.days

                # Convertir la diferencia en años, meses y días
                años = dias_retraso // 365
                dias_retraso %= 365
                meses = dias_retraso // 30
                dias_retraso %= 30

                prestamos.append(
                    f"{usuario}, {libro}, {fecha_prestamo}, ESTÁ CON MORA SOBREPASÓ FECHA LIMITE POR {años} AÑOS, {meses} MESES y {dias_retraso} DÍAS"
                )
            else:
                prestamos.append(f"{usuario}, {libro}, {fecha_prestamo}, NO TIENE MORA")

    return prestamos
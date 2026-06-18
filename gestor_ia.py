import csv
import json
import subprocess
import threading
from datetime import datetime
from pathlib import Path

class Recolector:
    def __init__(self):
        self.archivo_datos=Path("mis_preferencias.csv")
        self.columnas=["cancion","hora","dia_semana","mes","app_activa","y"]
        self.preparar_archivo()
    def preparar_archivo(self):
        if not self.archivo_datos.exists():
            with open(self.archivo_datos,mode="w",newline="",encoding="uft-8") as archivo:
                escritor=csv.writer(archivo)
                escritor.writerow(self.columnas)
            print(f"Se iniciado los datos en {self.archivo_datos}")


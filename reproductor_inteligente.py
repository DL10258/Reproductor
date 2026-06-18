from pathlib import Path
import keyword
import subprocess
import threading
import time

class Reproductor:
    def __init__(self):
        self.boveda_canciones = Path("/home/dragon/Música/")
        self.motor="./reproductor"
        self.formatos=[".mp3",".ogg",".flac",".wav"]
        self.canciones=list()
    def escanear_boveda(self):
        self.canciones=list()
        for archivo in self.boveda_canciones.rglob("*"):
            if archivo.is_file() and archivo.suffix.lower() in self.formatos:
                self.canciones.append(archivo)
        if not self.canciones:
            print(f"No se han detectado canciones en tu carpeta {self.boveda_canciones}")
    
    def reproducir(self):
        try:
            seleccion=int(input('Selecciona un canción: '))
            if 0<seleccion<=len(self.canciones):
                subprocess.run([self.motor,str(self.canciones[seleccion-1])],check=True)
                return True
            elif seleccion==0:
                return False
            else:
                print('Seleccione un valor valido')
                return True
        except ValueError:
            print("Digite un numero de la lista por favor")
            return True
        except KeyboardInterrupt:
            print("Se ha detenido la canción")
        except Exception as e:
            print(f"Ocurrio el sgte error {e}")
    def menu_canciones(self):
        self.escanear_boveda()
        if not self.canciones:
            return None
        while True:
            print('-'*40)
            for i,cancion in enumerate(self.canciones):
                print(f"[{i+1}] {cancion.name}")
            print(f'[0] Salir')
            print('-'*40)
            if not self.reproducir():
                print('Adios...')
                break
class Teclado:
    def __init__(self):
        self.siguiente
        self.stop
        self.anterior
        self.pausa

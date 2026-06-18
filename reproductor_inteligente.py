from pathlib import Path
import subprocess
import time
import threading
class Comandos:
    def __init__(self):
        self.params=["next","stop","help","salir","canciones"]
        self.datos={
            "next":"Para ir a la siguiente cancion.",
            "stop":"Detener la reproduccion",
            "help":"Mostrar ayuda."
        }
    def ayuda(self):
        for k,v in self.datos.items():
            print(f"{k}:{v}")
class Reproductor:
    def __init__(self):
        self.boveda_canciones = Path("/home/dragon/Música/")
        self.motor="./reproductor"
        self.formatos=[".mp3",".ogg",".flac",".wav"]
        self.canciones=list()
        self.estado_proceso=None
        self.indice_actual=0
    def escanear_boveda(self):
        self.canciones=list()
        for archivo in self.boveda_canciones.rglob("*"):
            if archivo.is_file() and archivo.suffix.lower() in self.formatos:
                self.canciones.append(archivo)
        if not self.canciones:
            print(f"No se han detectado canciones en tu carpeta {self.boveda_canciones}")
    def vigilar_reproduccion(self):
        while True:
            if self.estado_proceso!=None:
                if self.estado_proceso.poll() == None:
                    pass
                else:
                    if self.indice_actual==len(self.canciones)-1:
                        self.indice_actual=0
                    else:
                        self.indice_actual+=1
                    self.reproducir()
            else:
                pass
            time.sleep(1)
    def reproducir(self):
        if self.estado_proceso!=None:
            self.estado_proceso.kill()
        self.estado_proceso=subprocess.Popen([self.motor,str(self.canciones[self.indice_actual])])

    def menu_canciones(self):
        clase_comandos=Comandos()
        self.escanear_boveda()
        if not self.canciones:
            return None
        print('-'*40)
        for i,cancion in enumerate(self.canciones):
            print(f"[{i+1}] {cancion.name}")
        print(f'[0] Salir')
        print('-'*40)
        hilo_vigilancia=threading.Thread(target=self.vigilar_reproduccion)
        hilo_vigilancia.daemon=True
        hilo_vigilancia.start()
        while True:
            comando=input(">> ")
            if comando in clase_comandos.params:
                if comando == clase_comandos.params[0]: #comando next
                    if self.indice_actual==len(self.canciones)-1:
                        self.indice_actual=0
                    else:
                        self.indice_actual+=1
                    self.reproducir()
                elif comando == clase_comandos.params[1]: #comando stop
                    if self.estado_proceso!=None:self.estado_proceso.terminate()
                    self.estado_proceso=None
                elif comando == clase_comandos.params[2]: #comando help
                    clase_comandos.ayuda()
                elif comando == clase_comandos.params[3]: #comando salir
                    print("Adios...")
                    break
                elif comando == clase_comandos.params[4]: #comando canciones
                    print('-'*40)
                    for i,cancion in enumerate(self.canciones):
                        print(f"[{i+1}] {cancion.name}")
                        print(f'[0] Salir')
                    print('-'*40)
            elif comando.isdigit():
                if 0<=int(comando)-1<=len(self.canciones)-1:
                    self.indice_actual=int(comando)-1
                    self.reproducir()
                elif int(comando)==0:
                    print("Adios...")
                    break
                else:
                    print("Digita un numero correcto.Mas info con <canciones>")
            else:
                print("Comando no reconocido. Escriba <help> para mas informacion")

if __name__=="__main__":
    j_reproductor=Reproductor()
    j_reproductor.menu_canciones()

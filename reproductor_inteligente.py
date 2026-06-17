from pathlib import Path
import subprocess
ruta_canciones = Path("/home/dragon/Música")
reproducir = "./reproductor"
formatos=['.mp3','.ogg','.flac','.wav']
def reproduceme():
    canciones=list()
    for archivo in ruta_canciones.rglob("*"):
        if archivo.is_file() and archivo.suffix.lower() in formatos:
            canciones.append(archivo)
    if not canciones:
        print("No se encontraron canciones")
        return
    while True:
        print("-"*40)
        print("Canciones encontradas\n")
        print("-"*40)
        for i,cancion in enumerate(canciones):
            print(f"[{i+1}]{cancion.name}")
        print("[0]Salir")
        try:
            eleccion=int(input("Elige la cancion: "))
            if eleccion==0:
                print("Adios...")
                break
            elif 1<=eleccion<=len(canciones):
                cancion_selecionada=canciones[eleccion-1]
                print(f"Reproduciendo {cancion_selecionada.name}")
                subprocess.run([reproducir,str(cancion_selecionada)],check=True)
            else:
                print("Opcion no valida")
        except ValueError:
            print("Ingresa un número tarado.")
        except KeyboardInterrupt:
            print("Operacion anulada")
            break
        except Exception as e:
            print(f"Se detecto el siguiente error {e}")

if __name__=="__main__":
    if ruta_canciones.exists():
        reproduceme()
    else:
        print("No existe la carpeta seleccionada")

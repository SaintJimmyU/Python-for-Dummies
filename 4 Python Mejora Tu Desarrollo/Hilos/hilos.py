import threading # --> 
import time

class MiHilo(threading.Thread): # --> .Thread crea mis hilos
    def run(self) -> None: # --> run contendra el codigo que ejecutara .Thread
        print("{} inicio".format(self.getName))
        time.sleep(1) # --> Revisa a Detalle el Inicio y Final del Hilo . (1) significa 1 segundo ES UNA PAUSA
        print("{} Terminado".format(self.getName))

if __name__== "__main__":
    for x in range(4):
        hilo=MiHilo(name="Thread -> {}".format(x+1))
        print("Hilo # ",x+1)
        hilo.start()
        time.sleep(5)


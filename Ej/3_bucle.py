
import threading
import time
import os
                
pid = os.getpid() 
print(f"EL LEGENDARIO NUMEO DE PROCESO ES:{pid}")

#-----------------------HILO-------------------

def mi_funcion():
    for i in range(5):
        time.sleep(1)
        print("Hilo: Ejecución " + str(i))

# Crea un objeto Thread y pasa la función como objetivo
mi_hilo = threading.Thread(target=mi_funcion)

# Inicia la ejecución del hilo
mi_hilo.start()

# Espera a que el hilo termine antes de continuar con el programa principal
#mi_hilo.join()

print("Programa principal: El hilo ha terminado")

#-----------------------FIN HILO-------------------

def metodo3():
   while True:

       time.sleep(1)
       print("Mimiendo estoy")


#   METODO 3 (Bulce infinito):
buc = metodo3()
metodo3()
print (buc)

import random
import os

def separador():
    print("------------------")

def respuesta():
    print("Respuesta:")

class Menu():
    def __init__(self, juego, f):
        self.juego = juego
        self.f = f
    
    def mostrar_menu(self):
        separador()
        print("1) Iniciar partida")
        print("2) Ranking")
        print("3) Salir")  
        separador()
        respuesta() 

    def seleccionar(self):
        while True:
            self.mostrar_menu() 
            entrada = input()
            separador()   
            if entrada == "1":
                self.juego.numero()
                self.juego.logica()
            elif entrada == "2":
                print("Ranking")
                separador()
                self.f.read_file()
                separador()
                print("Presione ENTER para volver al menu")
                separador()
                nada = input()
            elif entrada == "3":
                break
            else:
                print("El valor que has puesto no es valido")
                separador()


class Juego():
    def __init__(self, f):
        self.numero_aleatorio = None
        self.f = f

    def numero(self):
        self.numero_aleatorio = random.randint(0, 9)

    def logica(self):
        puntos = 10
        print("Iniciando juego...")
        separador()
        print("Introduce tu nombre de Jugador")
        separador()
        nombre = input()
        separador()
        print("Escribe un numero del 0 al 9")
        separador()

        while True:
            elegir = "-1"
            elegir = input()  # convertir string a entero
            separador()
            if int(elegir) == self.numero_aleatorio:
                self.f.write_file([nombre, str(puntos)])
                print("Felicidades, Ganaste")
                print("Puntos:", puntos)
                separador()
                print("Presione ENTER para volver al menu")
                separador()
                nada = input()
                break
            else:
                print("Intenta de nuevo")
                separador()
                puntos -= 1

class TratamientoFichero():
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def write_file(self, data):
        with open(self.nombre_fichero, "a") as f:
            f.write(' '.join(map(str, data)) + "\n")
        
    def read_file(self):
        if os.path.exists(self.nombre_fichero):
            with open(self.nombre_fichero, "r") as f:
                print(f.read())
        else:
            print("El archivo no existe")
            print("Gana antes almenos una vez para que el archivo se cree")

# EJECUCION:

f = TratamientoFichero("prueba.txt")
j = Juego(f)
m = Menu(j, f)
m.seleccionar()  # Llama al método desde la instancia del menú

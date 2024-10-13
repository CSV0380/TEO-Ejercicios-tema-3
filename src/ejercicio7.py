##################### ---- LO QUE YO INTENTÉ ---- #########################

import random

def juego_adivina_numero(maximo):
  
    numero_aleatorio = random.randint(1, maximo)
    # print(f"El número a adivinar es: {numero_aleatorio}") #Para saber cual es

    while True:
       
        numero_usuario = int(input(f"Dime un número entero entre 1 y {maximo}: "))
        #metemos el numero del usuario dentro del while para que siga preguntando todo el rato pero sin crear un bucle infinito
       
        if numero_usuario < numero_aleatorio:
            print("El número a adivinar es mayor.")
        elif numero_usuario > numero_aleatorio:
            print("El número a adivinar es menor.")
        else:
            print(f"¡Has acertado! El número era {numero_aleatorio}.")
            break 





if __name__ == '__main__':

    numero_maximo = int(input("Dime el número máximo: "))
    juego_adivina_numero(numero_maximo)  
##################### ---- LO QUE YO INTENTÉ ---- #########################


'''
def imprime_pares(n):
    #crear una lista de números desde 0 hasta n inclyendo n(n+1)
    numeros = list(range(n + 1))  

    pares = [str(i) for i in numeros if i % 2 == 0 and i > 0]  #el str(i) sirve para que la i sea un string en lugar de una lista o algo
    
    resultado = " ".join(pares)
    print(resultado)



if __name__ == '__main__':

    while True:
        numero = int(input("Introduce un número entero mayor que 0: "))
        if numero > 0:
            break
        else:
            print("Por favor, introduce un número mayor que 0.")


    print(f"Imprimiendo números pares menores o iguales a {numero}:") #como python es secuencial ponemos el print luego del while true
    imprime_pares(numero) 



    
Es más lento porque gasta más memoria RAM ya que crea una lista, pero igualmente está bien

'''





##################### ---- LA SOLUCIÓN ---- #########################


def imprime_pares(n):
    # Crear una lista de números pares
    pares = [str(i) for i in range(2, n + 1, 2)]
    # Unir la lista en una cadena con espacios
    resultado = " ".join(pares)
    print(resultado)

# Ejemplo de uso
n1 = 5
print(f"Imprimiendo números pares menores o iguales a {n1}:")
imprime_pares(n1)  # Salida: 2 4

n2 = 6
print(f"Imprimiendo números pares menores o iguales a {n2}:")
imprime_pares(n2)  # Salida: 2 4 6

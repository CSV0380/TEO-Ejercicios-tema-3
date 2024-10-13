
##################### ---- LO QUE YO INTENTÉ (según el ejercicio anterior) ---- #########################



def imprime_pares_inverso(n):
    numeros = list(range(n + 1)) 

    pares = [i for i in numeros if i % 2 == 0 and i > 0] 
    pares.sort(reverse=True)  # Ordenar de mayor a menor

    
    resultado = " ".join(map(str, pares))  #el join lo que hace es unirlos y el map los transforma a string es equivalente a haber puesto en la lista de numeros el str(i)
    print(resultado)

if __name__ == '__main__':

    while True:
        numero = int(input("Introduce un número entero mayor que 0: "))
        if numero > 0:
            break  
        else:
            print("Por favor, introduce un número mayor que 0.")


    print(f"Imprimiendo números pares menores o iguales a {numero} en orden de mayor a menor:")
    imprime_pares_inverso(numero)
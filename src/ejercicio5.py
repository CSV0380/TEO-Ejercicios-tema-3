##################### ---- LO QUE YO INTENTÉ ---- #########################

'''
def indica_primera_aparicion(lista, valor):
    
    indice = lista.index(valor)
    if 

    else:
        print("El indice de la palabra en la lista es -1")



#tiene sentido lo que estoy haciendo ya que estoy utilizando el metodo index pero el profesor no quiere
'''


##################### ---- LA SOLUCIÓN ---- #########################


def indica_primera_aparicion(lista, valor):
    for indice, elemento in enumerate(lista): #enumeramos la lista 
        if elemento == valor:
            return indice  #devuelve el índice si encontramos(==) el valor
        else:
            return -1 




if __name__ == '__main__':
    lista1 = ["árbol", "coche", "casa", "peatón"]
    valor1 = "árbol"
    print(f"La posición de {valor1} en {lista1} es: {indica_primera_aparicion(lista1,valor1)}")

    valor2 = "bicicleta"
    print(f"La posición de {valor2} en {lista1} es: {indica_primera_aparicion(lista1,valor2)}")
##################### ---- LO QUE YO INTENTÉ ---- #########################


'''



def imprime_diccionario(diccionario):
    
    for c in diccionario:
        clave = c[0]
        valor = c[1]
        print(clave, "===>",valor)


if __name__ == '__main__':

    precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5}

    resultado = imprime_diccionario(precios_productos)


    
'''



##################### ---- LA SOLUCIÓN ---- #########################

def imprime_diccionario(diccionario):

    for clave, valor in diccionario.items():
        print(f"{clave} ===> {valor}")


if __name__ == '__main__':

    precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5}

    imprime_diccionario(precios_productos) #no hace falta crear una variable y luego printear la variable
    
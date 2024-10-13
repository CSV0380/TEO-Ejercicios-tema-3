##################### ---- LO QUE YO INTENTÉ ---- #########################



def calcula_precios(precio_entrada, lista_edad):

    precios = []
    for edad in lista_edad:

        if edad < 18 or edad > 65:
            precio_entrada_reducido = precio_entrada*0.5
            precios.append(precio_entrada_reducido)

        else:
            precios.append(precio_entrada)

    
    edades_str = ', '.join(map(str, lista_edad))  # Convertir las edades a string
    precios_str = ', '.join(map(str, precios))  # Convertir los precios a string
    print(f"Precios de las entradas para personas con edades {edades_str} (precio normal de la entrada: {precio_entrada}€):")
    print(precios_str)


if __name__ == '__main__':

    precio_entrada = 6.0  
    lista_edad = [8, 18, 25, 44, 64, 65, 70]  
    calcula_precios(precio_entrada, lista_edad)  



#Si quisieramos devolverlo como una lista seria mucho más fácil pero no entiendo por qué quieren complicarlo tan tontamente, sería algo así:

'''
def calcula_precios(precio_entrada, lista_edad):

    precios = []
    for edad in lista_edad:

        if edad < 18 or edad > 65:
            precio_entrada_reducido = precio_entrada*0,5
            precios.append(precio_entrada_reducido)

        else:
            precios.append(precio_entrada)

    return precios




if __name__ == '__main__':
    precio_entrada = 10.0  # Precio normal de la entrada
    lista_edad = [17, 25, 65, 70, 30]  # Edades de las personas
    precios_resultantes = calcula_precios(precio_entrada, lista_edad)
    print(precios_resultantes)

'''
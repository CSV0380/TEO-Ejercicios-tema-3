from collections import namedtuple
import csv
from datetime import datetime

Libro = namedtuple("Libro", "isbn, titulo, autor, fecha_publicacion, precio, disponible")


def lee_libros(ruta_csv): #parámetro es la ruta
    with open(ruta_csv, encoding="utf-8") as f: #abre el csv
        res = [] #una lista vacia para guardar el resultado
        lector = csv.reader(f) #lee el csv como f
        next(lector) #se salta la primera fila
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector: #por cada variable de la named en el csv lector
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date() #pones de que tipo es cada variable
            precio = float(precio) #aquí igual
            disponible = disponible == "Sí" 
            res.append(Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)) #añade a res todo lo que lee
        return res #guarda y devuelve res


# COMENTADO TODO LO QUE YO HICE:

'''
def autores_disponibles(libros, inicial):
    libros = []
    inicial = str(input("Dime la inicial: "))
    for autor, disponibilidad in lee_libros:
        
        if (inicial == Libro.autor[0]) and (disponibilidad == True):
            return libros.append(Libro(autor, disponibilidad))
    libros = sorted(libros)
    libros_sin_repe = set(libros)
    return libros_sin_repe
'''

def autores_disponibles(libros,inicial):
    autores = []
    for libro in libros:
        if libro.autor.startswith(inicial) and libro.disponible: #Usamos startswith() para comparar la primera letra
            autores.append(libro.autor)
    autores = sorted(set(autores))
    return autores



def titulos_baratos_actuales(libros):
    titulos_baratillos = []
    for i in libros:
        if (i.precio < 20.00) and (i.fecha_publicacion.year >= 2001):
            titulos_baratillos.append(i.titulo)
    return titulos_baratillos



def media_precios(libros, palabra):
    precios= []
    for libro in libros:
        if palabra in libro.titulo:
            precios.append(libro.precio)

    if not precios:
        return None
    
    precio_media = float(sum(precios) / len(precios))
    return precio_media



def libro_mas_reciente(libros):
    libro_reciente = max(libros, key=lambda libro: libro.fecha_publicacion)
    return libro_reciente







if __name__ == "__main__":

    libros = lee_libros("TEO-Ejercicios-tema-3\libreria.csv")
    print(f"Se han leído {len(libros)} libros.")


#Apartado 1:
    inicial_autor = str(input("Dime la incial del autor: "))
    print("Autores disponibles:", autores_disponibles(libros, inicial_autor))

#Apartado 2:
    print("Titulos baratos actuales:", titulos_baratos_actuales(libros))

#Apartado 3:
    palabra_clave = str(input("Dime la palabra clave: "))
    print(f"Media de precios de libros con la palabra {palabra_clave} : {media_precios(libros, palabra_clave)}")

#Apartado 4:
    print("Libro más reciente:", libro_mas_reciente(libros))

# Ejercicios del tema 3: Instrucciones condicionales y bucles
---

Cree una carpeta ``src``, y dentro de la misma un archivo ``ejercicioX.py`` para cada ejercicio que vaya a resolver, sustituyendo la X por el número del ejercicio. Implemente en cada archivo la función solicitada por el ejercicio correspondiente, asegurándose de que las pruebas de la función se realicen como programa principal.

## Ejercicio 1
Define una función llamada `fecha_en_intervalo` que acepte tres parámetros de tipo fecha: `fecha`, `fecha_min` y `fecha_max`. La función debe devolver `True` si `fecha` está dentro del rango definido por `fecha_min` y `fecha_max`, ambas inclusive. En caso de que `fecha_min` o `fecha_max` sean `None`, se omite la verificación correspondiente a esa parte del intervalo.

Pruebe la función con el siguiente código: 
```python
fecha_prueba = date(2024, 10, 2)

# Caso 1: fecha dentro del intervalo
print(fecha_en_intervalo(fecha_prueba, date(2024, 1, 1), ))  # True

# Caso 2: fecha fuera del intervalo (menor que fecha_min)
fecha_min = 
print(fecha_en_intervalo(fecha_prueba, date(2024, 10, 3), date(2024, 12, 31)))  # False

# Caso 3: fecha fuera del intervalo (mayor que fecha_max)
print(fecha_en_intervalo(fecha_prueba,None, date(2024, 9, 30)))  # False

# Caso 4: sin límite inferior (fecha_min es None)
print(fecha_en_intervalo(fecha_prueba, None, date(2024, 9, 30)))  # False

# Caso 5: sin límite superior (fecha_max es None)
print(fecha_en_intervalo(fecha_prueba, date(2024, 1, 1), None))  # True

# Caso 6: sin límites (fecha_min es None y fecha_max es None)
print(fecha_en_intervalo(fecha_prueba, None, None))  # True
```


## Ejercicio 2
Defina una función ``imprime_diccionario`` que imprima cada clave y cada valor del diccionario que recibe como parámetro, con el siguiente formato:
```
clave ===> valor
```

Pruebe la función pasándole este diccionario a la función: 
```python
precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5
}
```

## Ejercicio 3
Defina una función ``imprime_pares`` que reciba un entero ``n`` e imprima en la consola los números pares positivos menores o iguales a ``n``. Todos los números se deben imprimir en una sola línea, separados por espacios.

Pruebe la función de manera que se obtenga una salida parecida a esta:

```
Imprimiendo números pares menores o iguales a 5:
2 4 

Imprimiendo números pares menores o iguales a 6:
2 4 6
```


## Ejercicio 4
Implemente una función ``imprime_pares_inverso`` que funcione igual que la anterior pero imprima los números empezando por el mayor.

Pruebe la función de manera que se obtenga una salida parecida a esta:
```
Imprimiendo números pares menores o iguales a 5:
4 2 

Imprimiendo números pares menores o iguales a 6:
6 4 2
```

## Ejercicio 5
Defina una función ``indica_primera_aparicion`` que recibe un parámetro ``lista`` y un parámetro ``valor``, y devuelve el índice de la primera aparición de ``valor`` en ``lista``. Si no se encuentra ``valor`` en ``lista``, de devolverá ``-1``.

Pruebe la función de manera que se obtenga una salida parecida a esta:
```
Posición de "casa" en la lista ["árbol", "coche", "casa", "peatón"]: 2
Posición de "bicicleta" en la lista ["árbol", "coche", "casa", "peatón"]: -1
```

NOTA: Las listas en Python tienen un método parecido al que aquí estamos implementando (``index``), pero en este ejercicio no haremos uso de él.

## Ejercicio 6
Defina una función ``calcula_precios`` que reciba el precio de la entrada normal y una lista de enteros que representan las edades de una serie de personas y devuelva una lista con el precio de las entradas para cada una de las personas. Las personas con 65 o más años y las personas con 18 o menos años pagan un precio reducido del 50% del precio normal.

Pruebe la función de manera que se obtenga una salida parecida a esta:
```
Precios de las entradas para personas con edades 8, 18, 25, 44, 64, 65, 70 (precio normal de la entrada: 6€):
3.0, 3.0, 6.0, 6.0, 6.0, 3.0, 3.0
```



## Ejercicio 7
Implemente una función ``juego_adivina_numero`` que implemente el juego de adivinar un número aleatoriamente elegido. La función irá pidiendo números por teclado e informará al usuario de si el número que debe adivinar es mayor o menor que el introducido. Una vez que el usuario acierte el número, el juego acabará.

La función recibe un parámetro ``maximo``, de manera que el número a adivinar estará comprendido entre el 1 y ``maximo``. 

### Variaciones
* Haga que el juego cuente el número de intentos utilizados para adivinar el juego, e informe al usuario antes de acabar.
* Añada un número máximo de intentos, de manera que el juego finaliza si el usuario agota todos los intentos.

## Ejercicio 8

Complete el siguiente código para que se genere una lista con los nombres completos obtenidos de concatenar los nombres y apellidos de otras dos listas.

```python
nombres = ["Juan", "Ana", "Manuel", "Irene", "Jaime", "María"]
apellidos = ["Ruiz", "López", "Martínez", "Fernández", "Jiménez", "Castro"]
# La salida debe ser ['Juan Ruiz', 'Ana López', 'Manuel Martínez', 'Irene Fernández', 'Jaime Jiménez', 'María Castro']

nombres_completos = []
# TODO

print(nombres_completos)
```

## Ejercicio 9

Defina una función ``lee_personas``que reciba un entero ``n`` y lea el nombre y la edad de varias personas, devolviendo una lista de tuplas. Utilice la siguiente definición de ``namedtuple``:

```python
from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")
```

Prueba la función con este código:

```
n = 3
personas = lee_personas(n)
print(personas)
```

Implemente posteriormente las siguientes funciones:

* Función ``edad_media``, que recibe una lista de personas y devuelva la edad media.

* Función ``mayores_18``, que recibe una lista de personas y devuelva una lista ordenada alfabéticamente con los nombres de las personas mayores de edad.

* Función ``edades_distintas``, que recibe una lista de personas y devuelva una lista con las edades ordenadas de menor a mayor y sin duplicados.

* Función ``persona_mas_joven``, que reciba una lista de personas y devuelva el nombre de la persona de menor edad.

Pruebe cada una de las funciones pasándole la lista de personas leída anteriormente.

## Ejercicio 10
Tenemos un fichero CSV con registros de libros en una librería (se muestra la primera línea del fichero):

```
978-3-16-148410-0, El Gran Gatsby, F. Scott Fitzgerald, 10/04/1925, 12.99, True
```

Las columnas son:

* ISBN (str): Identificador único de cada libro.
* Título (str): Título del libro.
* Autor (str): Nombre del autor del libro.
* Fecha de publicación (date): Fecha en la que fue publicado el libro.
* Precio (float): Precio de venta en euros.
* Disponible (bool): Indica si el libro está en stock.

Se dispone de la namedtuple ``Libro`` para representar esta información (puede ver la definición en el módulo ``ejercicio10.py``).

Implemente las siguientes funciones:

* Función ``autores_disponibles``, que recibe una lista de libros y una cadena ``inicial`` y devuelve una lista ordenada alfabéticamente con los nombres de los autores cuya inicial es la indicada y para los que hay libros en stock en la librería. La lista no puede contener duplicados.

* Función ``titulos_baratos_actuales``, que recibe una lista de libros y devuelve una lista con los títulos de los libros con un precio inferior a 20 euros que hayan sido publicados a partir del año 2001.

* Función ``media_precios``, que recibe una lista de libros y una cadena de texto ``palabra`` y devuelve la media del precio de los libros que contienen en su título la ``palabra`` en cuestión. Si no se encuentra ningún libro con dicha palabra en el título, la función devuelve ``None``. **NOTA**: La búsqueda de los libros con la palabra en el título no debe ser sensible a mayúsculas.

* Función ``libro_mas_reciente``, que recibe una lista de libros y devuelve el libro con la fecha de publicación más reciente.

Al probar las funciones, debe obtener una salida parecida a esta:

```
Autores disponibles que comienzan por 'M': ['Margaret Atwood', 'Margaret Mitchell', 'Mark Twain', 'Miguel de Cervantes']
Titulos baratos actuales: ['La carretera', 'La sombra del viento', 'La chica con el tatuaje de dragón', 'La chica del tren']
Media de precios de libros con la palabra 'El': 25.093571428571426
Libro más reciente: Libro(isbn='978-3-16-392611-0', titulo='La chica del tren', autor='Paula Hawkins', fecha_publicacion=datetime.date(2015, 1, 13), precio=8.34, disponible=False)
```
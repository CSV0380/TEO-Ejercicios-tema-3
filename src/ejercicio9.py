##################### ---- LO QUE YO INTENTÉ ---- #########################

from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    personas = []
    for i in range(n):
        nombre = input("Introduce el nombre: ")
        edad = int(input("Introduce la edad: "))
        persona = Persona(nombre, edad)
        personas.append(persona)
    return personas



def edad_media(personas):
    total_edad = sum(persona.edad for persona in personas)
    return total_edad / len(personas)



def mayores_18(personas):
    return sorted(persona.nombre for persona in personas if persona.edad >= 18)



def edades_distintas(personas):
    conjunto_edades = set(persona.edad for persona in  personas) #si creas un conjunto ya no se repiten los elementos
    return sorted(conjunto_edades)



def persona_mas_joven(personas):
    conjunto_joven = set(persona.edad for persona in personas)
    conjunto_joven = sorted(conjunto_joven)
    primer_joven = list(conjunto_joven)[0]
    return primer_joven

# def persona_mas_joven(personas):
#     persona_joven = min(personas, key=lambda p: p.edad)
#     return persona_joven.nombre

if __name__ == '__main__':

    n = 2
    personas = lee_personas(n)
    print("\nLista de personas:", personas)
    
    media = edad_media(personas)
    print(f"Edad media: {media:.2f}")

    mayores = mayores_18(personas)
    print("Nombres de personas mayores de 18:", mayores)

    distintas = edades_distintas(personas)
    print("Edades distintas ordenadas:", distintas)

    joven = persona_mas_joven(personas)
    print("La persona más joven es:", joven)

#'Juan Ruiz', 'Ana López', 'Manuel Martínez', 'Irene Fernández', 'Jaime Jiménez', 'María Castro'

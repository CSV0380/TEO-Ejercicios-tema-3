    ##################### ---- LO QUE YO INTENTÉ ---- #########################


if __name__ == '__main__':

    nombres = ["Juan", "Ana", "Manuel", "Irene", "Jaime", "María", "Julio "]
    apellidos = ["Ruiz", "López", "Martínez", "Fernández", "Jiménez", "Castro"]

    nombres_completos = []

    for nombre, apellidos in zip(nombres, apellidos): #el zip lo que hace es unirlos, combina el primer nombre con el primer apellido y asi sucesivamente
        nombres_completos.append(f"{nombre} {apellidos}")

    print(nombres_completos)



##################### ---- LO QUE YO INTENTÉ ---- #########################


'''
from datetime import date
from datetime import datetime

def fecha_en_intervalo(fecha,fecha_min = None,fecha_max = None):
    fecha, fecha_min, fecha_max = datetime.strptime(fecha, fecha_min, fecha_max, "%d/%m/%Y").date()
    if fecha >= fecha_min and fecha <= fecha_max:
        return True
    else:
        return None
    

fecha_prueba = date(input("Dime una fecha: ")) #Esto no funcionaria ya que el input lo pone como una cadena y no como un date
fecha_minima =                                 #la solución es ponerlo en modo datetime, así: fecha_prueba = input("Dime una fecha (dd/mm/yyyy): ")
fecha_prueba =                                 #datetime.strptime(fecha_prueba, "%d/%m/%Y").date()
fecha_en_intervalo(fecha_prueba)
'''




##################### ---- LA SOLUCIÓN ---- #########################

from datetime import date
    

def fecha_en_intervalo(fecha, fecha_min=None, fecha_max=None): #igualarlo a None es para darle un valor en caso de que nunca tome ninguno
    
    if (fecha_min is not None and fecha <= fecha_min) and (fecha_max is not None and fecha >= fecha_max):
        return False
    else:
        return True



if __name__ == '__main__':

    fecha_prueba = date(2024, 10, 2)

    resultado1 = fecha_en_intervalo(fecha_prueba, date(2024, 1, 1), None)
    print(f"¿Está la fecha dentro del intervalo? {resultado1}")
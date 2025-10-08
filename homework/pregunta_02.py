"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter
lectura = open("files/input/data.csv", "r").readlines()
limpieza1 = [z.replace('\n', '') for z in lectura]
limpieza2 = [z.replace('\t', ',') for z in limpieza1]
limpieza3 = [z.split(',') for z in limpieza2]

def pregunta_02():
    lista = []
    for z in limpieza3:    
        #print(z[:2])
        lista.append((z[0]))
        #print(lista)
        
    lista  

    # Y si quiero contar todos los elementos que tengo en la lista? ("a",4), ("b",5)
    resultado = sorted(list(Counter(lista).items()))
    return resultado

print(pregunta_02())

"""    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
"""
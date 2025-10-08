"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

lectura = open("files/input/data.csv", "r").readlines()
limpieza1 = [z.replace('\n', '') for z in lectura]
limpieza2 = [z.replace('\t', ',') for z in limpieza1]
limpieza3 = [z.split(',') for z in limpieza2]

"""print(limpieza2)
print(limpieza3)
limpieza3[0][1]"""



def pregunta_01():
    suma=0
    for z in limpieza3:    
        suma+= int(z[1])
        

    suma
            
    return suma
print(pregunta_01())
import random
import json


with open('participantes.json','r') as archivo:
    participantes = json.load(archivo)

# 3. Sorteo aleatorio
nombres = [p["nombre"] for p in participantes]

def asignar_amigo_secreto(nombres):
    asignaciones = None
    while not asignaciones:
        asignados = nombres[:]
        random.shuffle(asignados)
        
        if all(nombres[i] != asignados[i] for i in range(len(nombres))):
            asignaciones = {nombres[i]: asignados[i] for i in range(len(nombres))}
            
    return asignaciones

print(asignar_amigo_secreto(nombres))
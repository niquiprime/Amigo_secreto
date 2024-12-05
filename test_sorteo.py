import random

participantes = [
    {"nombre": "Ana", "numero": "whatsapp:+56912345678"},
    {"nombre": "Luis", "numero": "whatsapp:+56987654321"},
    {"nombre": "María", "numero": "whatsapp:+56911223344"},
    {"nombre": "Carlos", "numero": "whatsapp:+56955667788"}
]

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
    
asignaciones = asignar_amigo_secreto(nombres)

print(asignaciones)
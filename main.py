from twilio.rest import Client
from dotenv import load_dotenv
import os
import random
import json

# Cargar variables de entorno
load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('TOKEN_AUTH')

try:
    client = Client(account_sid, auth_token)
except Exception as e:
    print(f"Error inicializando el cliente Twilio: {e}")
    exit()

# Cargar el archivo JSON
try:
    with open('participantes.json', 'r') as archivo:
        participantes = json.load(archivo)
except FileNotFoundError:
    print("Error: El archivo 'participantes.json' no se encontró.")
    exit()
except json.JSONDecodeError as e:
    print(f"Error al leer el archivo JSON: {e}")
    exit()

# 3. Sorteo aleatorio
try:
    nombres = [p["nombre"] for p in participantes]
except KeyError as e:
    print(f"Error: Falta una clave esperada en los datos de los participantes: {e}")
    exit()

def asignar_amigo_secreto(nombres):
    asignaciones = None
    while not asignaciones:
        asignados = nombres[:]
        random.shuffle(asignados)
        
        if all(nombres[i] != asignados[i] for i in range(len(nombres))):
            asignaciones = {nombres[i]: asignados[i] for i in range(len(nombres))}
            
    return asignaciones

try:
    asignaciones = asignar_amigo_secreto(nombres)
except Exception as e:
    print(f"Error durante el sorteo de amigos secretos: {e}")
    exit()

# 4. Enviar mensajes
for participante in participantes:
    try:
        amigo_secreto_nombre = asignaciones[participante["nombre"]]

        # Buscar los detalles del amigo secreto
        amigo_secreto = next(p for p in participantes if p["nombre"] == amigo_secreto_nombre)
        opciones_regalo = "\n".join([f"{i + 1}. {opcion}" for i, opcion in enumerate(amigo_secreto["opciones_regalo"])])

        mensaje =f"¡Hola *{participante['nombre']}*! 🎅 Tu amigo secreto es: *{amigo_secreto_nombre}* !!.\n\n Estas son sus opciones de regalo para el/ella: \n{opciones_regalo} 🎁\n\n ¡No se lo digas a nadie! 🤫 *TESTING*" 

        message = client.messages.create(
            body=mensaje,
            from_='whatsapp:+14155238886',
            to=participante["numero"]
        )
        print(f"Mensaje enviado a {participante['nombre']}: SID {message.sid}")

    except KeyError as e:
        print(f"Error: Clave faltante en los datos del participante o amigo secreto: {e}")
    except StopIteration:
        print(f"Error: No se encontró el amigo secreto para {participante['nombre']}")
    except Exception as e:
        print(f"Error enviando el mensaje a {participante['nombre']}: {e}")
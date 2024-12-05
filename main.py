import random
from twilio.rest import Client

# 1. Configuración de Twilio
TWILIO_ACCOUNT_SID = "tu_account_sid"
TWILIO_AUTH_TOKEN = "tu_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Número de Twilio

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# 2. Lista de participantes (nombre, número de WhatsApp)
participantes = [
    {"nombre": "Ana", "numero": "whatsapp:+56912345678"},
    {"nombre": "Luis", "numero": "whatsapp:+56987654321"},
    {"nombre": "María", "numero": "whatsapp:+56911223344"},
    {"nombre": "Carlos", "numero": "whatsapp:+56955667788"}
]

# 3. Sorteo aleatorio
nombres = [p["nombre"] for p in participantes]
random.shuffle(nombres)
asignaciones = {participantes[i]["nombre"]: nombres[(i + 1) % len(nombres)] for i in range(len(participantes))}

# 4. Enviar mensajes
for participante in participantes:
    amigo_secreto = asignaciones[participante["nombre"]]
    mensaje = f"¡Hola {participante['nombre']}! Tu amigo secreto es: {amigo_secreto}. ¡No se lo digas a nadie! 🎅🎁"
    
    message = client.messages.create(
        body=mensaje,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=participante["numero"]
    )
    print(f"Mensaje enviado a {participante['nombre']}: SID {message.sid}")
from twilio.rest import Client
from dotenv import load_dotenv
import os
import time  # Para agregar el delay

# Cargar variables de entorno
load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('TOKEN_AUTH')
client = Client(account_sid, auth_token)

mensaje3 = "Te amo pq eres mi compañera, me acompañas y me amas mucho. Porque me gusta mucho tu compañia y se me hace corto el dia contigo"
a = 0

# Cambiar la condición del bucle para ejecutarse correctamente
while a < 1:
    message = client.messages.create(
        body=mensaje3,
        to="whatsapp:+56982187112",
        from_='whatsapp:+14155238886'
    )
    print(f"Mensaje enviado {a + 1}: {message.sid}")
    a += 1  # Corregir el incremento
    time.sleep(1)  # Agregar un delay de 1 segundo

# Proyecto de Amigo Secreto con WhatsApp y Twilio

Este proyecto permite realizar un sorteo de amigo secreto y notificar a cada participante a través de mensajes de WhatsApp utilizando la API de Twilio.

---

## **Requisitos previos**

1. Tener instalado **Python 3.8 o superior**.
2. Contar con acceso a un número de WhatsApp configurado en Twilio.
3. Clonar o descargar este repositorio en tu computadora.

---

## **Configuración del entorno**

1. **Clonar el repositorio**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>

2. **Crear entorno virtual (OPT)**
    ```bash
        python -m venv venv
        source venv/bin/activate    # En Linux/Mac
        venv\Scripts\activate       # En Windows

3. **Instalar Dependecias**
    ```bash
    pip install -r requirements.txt

# Crea y reemplaza .env
    TWILIO_ACCOUNT_SID=tu_account_sid
    TWILIO_AUTH_TOKEN=tu_auth_token
    TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886


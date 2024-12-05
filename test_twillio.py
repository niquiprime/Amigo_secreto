from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('TOKEN_AUTH')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body= '*cagaste* papito',
  to= os.getenv('PHONE_NUMBER')
)

print(message.sid)
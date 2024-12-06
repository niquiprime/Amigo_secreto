from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('TOKEN_AUTH')
client = Client(account_sid, auth_token)

message = client.messages.create(
  body='*cagaste* papito',
  media_url=["https://demo.twilio.com/owl.png"],
  to= os.getenv('PHONE_NUMBER'),
  from_='whatsapp:+14155238886'
)

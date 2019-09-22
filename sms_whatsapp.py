from twilio.rest import Client
from config import *


account_sid = account_sid
auth_token = auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hola niña boba',
                              from_='whatsapp:' + whatsapp_number_sender,
                              to='whatsapp:' + my_number
                          )

print(message.sid)
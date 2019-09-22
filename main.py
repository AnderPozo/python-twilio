from twilio.rest import Client
from config import *

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = my_number, 
    from_ = sender_number,
    body ="Hello from Python!")

print(message.sid)

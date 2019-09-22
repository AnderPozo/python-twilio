from twilio.rest import Client
from config import *

account_sid = account_sid
auth_token = auth_token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         media_url=['https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/main_element/public/media/image/2019/08/poster-star-wars-ascenso-skywalker_0.jpg?itok=6vbRl6Bs'],
         from_='whatsapp:' + whatsapp_number_sender,
         body="Star Wars Episode 9",
         to='whatsapp:' + my_number
     )

print(message.sid)

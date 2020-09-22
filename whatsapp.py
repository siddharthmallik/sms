from twilio.rest import Client

account_sid = 'AC5ca388661f220c59aede71464b7b22a8'
auth_token = 'dfc895772065466686f143de6fa9bfdb'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello,Tom,Whatsup',
    to='whatsapp:+917809497985'
)

print(message.sid)

from twilio.rest import Client
account_sid = 'account_id'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+16203038645',
    body='Alert ',
    to='+918076007125'
    )

    print(message.sid)
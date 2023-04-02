# To send smsm you have to login in https://www.twilio.com

from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

mess = client.messages.create(
    body="siemanko",
    from_ = keys.twilio_number,
    to = keys.ratger_number
)

print(mess.body)
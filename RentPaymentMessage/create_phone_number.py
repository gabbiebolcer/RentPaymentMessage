"""Run this module ONCE to create a twilio phone number to send messages from. Will write the phone num to creds.py"""
from twilio.rest import Client
from creds import account_sid_test, auth_token_test


account_sid = account_sid_test
auth_token = auth_token_test


def create_phone_number(*, phone_number: str = '+15005550006'):
    client = Client(account_sid, auth_token)

    incoming_phone_number = client.incoming_phone_numbers \
        .create(
             phone_number=phone_number,
             voice_url='http://demo.twilio.com/docs/voice.xml'
         )

    print(incoming_phone_number.sid)

    with open("creds.py", "a") as c:
        c.write(f"\ntwilio_phone_num = '{phone_number}'")


if __name__ == "__main__":
    create_phone_number(phone_number='+15005550006')



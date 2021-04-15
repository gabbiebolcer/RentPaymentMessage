
import pandas
from twilio.rest import Client

from creds import account_sid_test, auth_token_test, twilio_phone_num

account_sid = account_sid_test
auth_token = auth_token_test


def send_message(rent_to: str = "Gabbie"):
    client = Client(account_sid, auth_token)

    names_and_nums = pandas.read_excel('namesandnumbers.xlsx')

    for number, name in names_and_nums.iterrows():
        phone_num = name['PhoneNum']
        person = name['Name']
        message = client.messages.create(
            to=phone_num,
            from_=twilio_phone_num,
            body=f"Hi {person}, this is a reminder to send your rent to {rent_to} within the next few days! thanks!!",
        )

if __name__ == "__main__":
    send_message("Gabbie")

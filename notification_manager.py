from twilio.rest import Client
import os


account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["API_KEY"]
twilio_virtual_number = os.environ["TWILIO_NUMBER"]
twilio_verified_number = os.environ["PERSONAL_NUMBER"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self,):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_virtual_number,
            to=twilio_verified_number
        )
        print(message.sid)
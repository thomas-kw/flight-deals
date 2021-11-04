from twilio.rest import Client
import os


account_sid = "AC4bc9d655663dcdcdbee672f007fc79d9"
auth_token = os.environ["API_KEY"]
twilio_virtual_number = "+13195058865"
twilio_verified_number = "+821046321383"


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
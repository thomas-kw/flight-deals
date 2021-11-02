from twilio.rest import Client

account_sid = "AC4bc9d655663dcdcdbee672f007fc79d9"
auth_token = "76cc01232de49544b5f41c170fe90cc2"

client = Client(account_sid, auth_token)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, price, destination):
        self.price = price
        self.destination = destination

    def send_message(self):
        if self.price < 30:
            message = client.messages.create(
                body=f"There is a good deal for a flight! Price: {self.price}. Destination: {self.destination}",
                from_="+13195058865",
                to='+821046321383'
            )
            print(message.sid)

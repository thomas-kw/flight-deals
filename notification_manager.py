import smtplib
from twilio.rest import Client
import os

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["API_KEY"]
twilio_virtual_number = os.environ["TWILIO_NUMBER"]
twilio_verified_number = os.environ["PERSONAL_NUMBER"]

MY_EMAIL = "email@email.com"
MY_PASSWORD = "12345678"


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

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="placeholder@email.com",
                    msg=f"Subject:New Low Price!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )



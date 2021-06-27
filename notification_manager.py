from twilio.rest import Client
import smtplib


# twillo details

TWILIO_SID = "ACfc1f66926937dff5407161913da6f046"
TWILIO_AUTH_TOKEN = "ed4dd63eb483ccfa012c4ed39c222058"
TWILIO_VIRTUAL_NUMBER = "+18303411303"
TWILIO_VERIFIED_NUMBER = "+85290986832"

# --- yahoo smtp server
MY_EMAIL = "yukwokng@yahoo.com"
PASSWORD = "lkgpczgtbyunkabs"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails=[], coming_cheapest=""):

        if emails != []:
            for receiver_email in emails:
                with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
                    connection.starttls()
                    connection.login(
                        user=MY_EMAIL, password=PASSWORD)   # --- auth
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=receiver_email,
                                        msg=f"Subject: coming 6 months cheapest flights"
                                            f"\n\n"
                                            f"{coming_cheapest}")

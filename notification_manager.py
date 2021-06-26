from twilio.rest import Client

# twillo details

TWILIO_SID = "ACfc1f66926937dff5407161913da6f046"
TWILIO_AUTH_TOKEN = "ed4dd63eb483ccfa012c4ed39c222058"
TWILIO_VIRTUAL_NUMBER = "+18303411303"
TWILIO_VERIFIED_NUMBER = "+85290986832"


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

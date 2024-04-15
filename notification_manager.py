from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.account_sid = ""
        self.auth_token = ""
        self.client = Client()

    def send_sms(self, result):
        print(result)
        message = self.client.messages.create(
            body=result,
            from_="+12058093489",
            to="+37369467775",
        )


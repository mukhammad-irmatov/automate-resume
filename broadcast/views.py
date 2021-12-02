from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

account_sid = "ACfe40a932a05078e5b02a581d9987a351"
# Your Auth Token from twilio.com/console
auth_token  = "31fac19a8c8c75a378db34016d22d4a9"
def broadcast_sms(request):
    message_to_broadcast = ("Assalomu aleykum, sizga intervyu belgilangan. Intervyu vaqti Chorshanba kuni soat 11:30da ")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
from django.shortcuts import render
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from twilio.rest import Client
from user.models import User
import urllib.parse as urlparse
from urllib.parse import parse_qs

def broadcast_sms(request):
    # # print()
    # print(str(request) + "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55")
    # parse = urlparse.urlparse(request)
    # print(parse_qs(parsed.query)['id'] + "%%%%%%%%%%%%%%%%%%&&&&&&&&&")
    # # print()
    # print(request.GET.get('id')+ "%%%%%%%%%%%%%%%%%%&&&&&&&&&")
    id = request.GET.get('id')
    recipient = User.objects.filter(id=id).first()
    message_to_broadcast = ("Dear " + recipient.member.name + ",\nYour registration with Panha Foundation has been completed successfully!")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    if recipient:
        cm = str(recipient.contact)
       	client.messages.create(to=cm,
                               from_=settings.TWILIO_NUMBER,
                               body=message_to_broadcast)
    return redirect(login)
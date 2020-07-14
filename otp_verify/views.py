API_KEY = "tBAaL7yY4xPhuM5HDrwmdRkgUof1QbXGq2VlEj6IKF8TcWNZz9xhNoZfytH4PG0qdz761rAC9QXnsvJ2"
SENDER_ID = "FSTSMS"
from django.shortcuts import render
# Create your views here.

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView

import base64

import requests

class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret"


class getPhoneNumberRegistered(APIView):
    @staticmethod
    def get(request):
        phone = int(request.GET['phone']);
        counter = int(request.GET['counter']);
        keygen = generateKey();
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.HOTP(key)
        otp_string = OTP.at(counter)
        url = "https://www.fast2sms.com/dev/bulk"
        var_values = str(phone) + "|" + str(otp_string)
        querystring = {
            "authorization": API_KEY,
            "sender_id" : SENDER_ID,
            "language": "english",
            "route": "qt",
            "numbers" : str(phone), 
            "message" : "31395",
            "variables" : "{#CC#}|{#BB#}",
            "variables_values" : var_values
        }
        headers = {
            "cache-control" : "no-cache"
        }
        response = requests.request("GET", url , headers = headers, params = querystring)
        print(otp_string)
        return Response({"OTP" : otp_string}, status = 200)

    @staticmethod
    def post(request):
        phone = int(request.data['phone']);
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.HOTP(key) 
        if OTP.verify(int(request.data['otp']) , int(request.data['counter'])):
            return Response("You are authorized", status = 200)
        return Response("OTP is wrong", status = 400)    

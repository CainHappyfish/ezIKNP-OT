from django.shortcuts import render 
from ot.sender import Sender

def sender(request):
    s = Sender()
    RandomStr = s.genRandomString(16)
    
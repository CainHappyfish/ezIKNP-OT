from receiver import *
from django.http import HttpResponse
def hello(request):
    return HttpResponse("this is Alice")

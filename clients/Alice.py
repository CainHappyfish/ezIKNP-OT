from receiver import *
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("this is Alice")

def RenderTest(request):
    context = {}
    context["test"] = "Render Test"
    return render(request, "test.html", context)

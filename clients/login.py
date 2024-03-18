from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
    if request.POST:
        return HttpResponseRedirect("/receiver/")
    else:
        return render(request, "login.html")
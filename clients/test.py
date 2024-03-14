from django.shortcuts import render

def test(request):
    context = {}
    context["test"] = "Test"
    return render(request, "test.html", context)
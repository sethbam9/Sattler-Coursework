from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def greet(request, name):
#     return HttpResponse(f"<h1 style=\"color:blue\">Hello, {name}!</h1>")
def greet(request, name):
    return render(request, "my_app/greet.html", {
        "name": name.capitalize()
    })

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def index(request):
    return render(request, "my_app/index.html")

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

pages = ['About', 'Contact', 'Projects']
fname = "Seth"
lname = "Howell"

# Create your views here.
def home_view(request, *args, **kwargs):
    print(f"args: {args}\nkwargs: {kwargs}")
    print(f"user: {request.user}")
    my_context = {
        'pages': pages,
        'name' : fname + " " + lname,
        'my_list': ["mommy", "made", "me", "mash", "my", "eminems"]
    }
    return render(request, "home.html", my_context)  # HttpResponse("<h1>Seth Howell</h1>")

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def projects_view(request, *args, **kwargs):
    return render(request, "project.html", {})

from django.shortcuts import render
from django.core.paginator import Paginator


from .models import Vehicle, Make

# Create function for page render to avoid duplicating code
def render_with_pagination(request, vehicles):
    page_num = request.GET.get('page', 1) #if not found, assign 1
    paginator = Paginator(vehicles, 2) # FOR PROJECT USE 10
    page = paginator.page(page_num)

    return render(request, "marketplace/index.html", {'page':page})


def index(request):

    #Get all vehicles
    vehicles = Vehicle.objects.all()

    return render_with_pagination(request, vehicles)


def make(request, id): # make id

    # Option 1 - BAD
    # make = Make.objects.get(pk=1)
    # vehicles = Vehicle.objects.filter(make=make)

    # Option 2 - better
    # vehicles = Vehicle.objects.filter(make__id=id)
        # double underscore __ says -> where make's id == id.

    # Option 3 - best: use related_name make.vehicles
    make = Make.objects.get(pk=id)

    return render_with_pagination(request, make.vehicles.all())

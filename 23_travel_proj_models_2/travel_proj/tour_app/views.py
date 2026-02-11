from django.shortcuts import render

from .models import Destination


# Create your views here.
def landing(request):
    context = {
        "dests": Destination.objects.filter(is_featured=True)
    }
    return render(request,
                  "tour_app/landing.html",
                  context=context)

def destination(request, id):
    context = {
        "dest": Destination.objects.get(id=id)
    }
    return render(request,
                  "tour_app/destination.html",
                  context=context)
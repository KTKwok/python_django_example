from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "welcome": "Welcome to Travel Proj",
    }
    return render(request,
                  'public_app/index.html',
                  context=context)

def about(request):
    context = {}
    return render(request,
                  'public_app/about.html',
                  context=context)
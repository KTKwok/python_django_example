from django.shortcuts import render
from django.views import View


# Create your views here.
def index(request):
    context = {
        "welcome": "Welcome to Travel Proj",
    }
    return render(request,
                  'public_app/index.html',
                  context=context)

class About(View):
    def get(self, request, *args, **kwargs):
        fullname = request.GET.get('fullname', 'Guest')
        context = {
            "fullname": fullname,
        }
        return render(request,
                      'public_app/about.html',
                      context=context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        context = {
            "email": email,
            "comment": comment
        }
        return render(request,
                      'public_app/contact_us_submitted.html',
                      context=context)
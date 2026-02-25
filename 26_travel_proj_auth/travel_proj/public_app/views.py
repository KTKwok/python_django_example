from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

from .decorators import allowed_user


# Create your views here.
def index(request):
    context = {
        "welcome": "Welcome to Travel Proj",
    }
    return render(request,
                  'public_app/index.html',
                  context=context)

@login_required
@allowed_user(allowed_roles=['M'])
def company_org_chart(request):
    context = {

    }
    return render(request,
                  "public_app/company_org_chart.html",
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
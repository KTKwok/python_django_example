from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from .decorators import allowed_user, unauthenticated_user_only
from .forms import UserProfileForm, SignUpForm
from .models import UserProfile


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

@unauthenticated_user_only
def sign_up(request):
    form = SignUpForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created for '{}'".format(user.username))
            return redirect("public_app:edit_profile")

    context={
        "form":form
    }
    return render(request,
                  'public_app/signup.html',
                  context=context)

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user,
                                                         defaults={
                                                             "bio": "I am so smart",
                                                         })

    form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, "Profile updated successfully")
            return redirect("public_app:index")

    context = {
        "created":created,
        "form": form
    }
    return render(request,
                  'public_app/edit_profile.html',
                  context=context)
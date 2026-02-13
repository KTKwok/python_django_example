from django.shortcuts import render

from .forms import AuthorForm
from .models import Author


# Create your views here.
def index(request):

    context = {
        "authors": Author.objects.all()
    }
    return render(request,
                  template_name='store_app/index.html',
                  context=context)

def create_author(request):
    context={}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        author = Author.objects.create(first_name=first_name,
                              last_name=last_name,
                              email=email)

        context = {
            "author": author
        }
    return render(request,
                  template_name='store_app/create_author.html',
                  context=context)

def create_author_form(request):
    form = AuthorForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()

    context = {
        "form": form
    }
    return render(request,
                  template_name='store_app/create_author_form.html',
                  context=context)

def update_author_form(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(request.POST or None, instance=author)
    if request.method == "POST":
        if form.is_valid():
            form.save()

    context = {
        "form": form
    }
    return render(request,
                  template_name='store_app/create_author_form.html',
                  context=context)


def get_or_create_author(request):
    author, created = Author.objects.get_or_create(first_name='Tim',
                                          defaults={
                                              "last_name":'Liu',
                                              "email":'tim.liu@example.com'
                                          })

    context = {
        "author": author,
        "created": created
    }
    return render(request,
                  template_name='store_app/get_or_create_author.html',
                  context=context)
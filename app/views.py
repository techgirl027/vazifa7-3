from django.shortcuts import render
from app.models import *

# Create your views here.


def home_page(request):
    comments = Comments.objects.all()
    services = Services.objects.all()
    context = {
        "comments": comments,
        "services": services,
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        models.Contact.objects.create(name=name, email=email, message=message)
    return render(request, "contact.html")


def service(request):
    services = Services.objects.all()
    context = {
        "services": services,
    }
    return render(request, "service.html", context)

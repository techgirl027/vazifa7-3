from django.shortcuts import render
from .models import Services, Contact, Comments
from app import models

# Create your views here.


def home_page(request):
    return render(request, "index.html")


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

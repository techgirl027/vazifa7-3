from app.views import *
from django.urls import path

# from . import views


urlpatterns = [
    path("", home_page, name="home_page"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("service/", service, name="service"),
]

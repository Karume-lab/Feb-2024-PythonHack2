from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", views.home, name="home"),
]

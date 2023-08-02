from django.urls import path
from fibonacci_generator import views

urlpatterns = [
    path("", views.index, name="index"),

]
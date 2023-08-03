from django.urls import path
from fibonacci_generator import views


urlpatterns = [
    path("", views.user_input, name="input"),
    path("output", views.display_output, name="output"),

]
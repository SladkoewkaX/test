from django.urls import path

from .views import show_text

# app_name = "Django_test"


urlpatterns = [
    path('', show_text),
]
from django.urls import path

# IMPORT VIEWS
from . import views

urlpatterns = [
    path('', views.api_home)
]


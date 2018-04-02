from django.urls import path

from . import views

urlpatterns = [
    # views.index => Python syntax on calling function
    path('', views.index, name='index'),
]


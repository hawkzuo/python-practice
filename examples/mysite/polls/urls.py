from django.urls import path

from . import views

urlpatterns = [
    # views.index => Python syntax on calling function
    path('', views.index, name='index'),
    path('json_request', views.json_request, name='json')
]


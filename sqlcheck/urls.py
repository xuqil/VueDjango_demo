from django.urls import path
from . import views

app_name = 'sqlcheck'

urlpatterns = [
    path('', views)
]
from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('front/', views.index, name='front'),
    path('add_book/', views.add_book, name='add_book')
]

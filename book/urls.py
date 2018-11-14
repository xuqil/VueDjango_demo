from django.urls import path
from book import views

app_name = 'book'

urlpatterns = [
    path('', views.index),
    path('detail<book_id>/<book_idd>', views.book),
    path('book/author', views.author_detail),
]

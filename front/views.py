from django.shortcuts import render
from django.db import connection


def get_cursor():
    return connection.cursour


def index(request):
    return render(request, 'index.html')


def add_book(request):
    return render(request, 'add_book.html')


def book_detail(request):
    return render(request, 'book_detail.html')


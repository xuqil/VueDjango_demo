from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("你好")


def book(request, book_id,book_idd):
    text = "你的书ID:" + book_id + book_idd
    return HttpResponse(text)
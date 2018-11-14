from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    # html = render_to_string("index.html")
    return render(request, 'index.html')


def book(request, book_id, book_idd):
    text = "你的书ID:" + book_id + book_idd
    return HttpResponse(text)


def author_detail(request):
    # author_id = request.GET['id']
    author_id = request.GET.get('id')
    text = 'id:%s' % author_id
    return HttpResponse(text)
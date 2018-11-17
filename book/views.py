from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Book


class Person(object):
    def __init__(self, username):
        self.username = username


def index(request):
    # p = Person("花红")
    # context = {
    #     'person': p
    # }
    context = {
        # 'person': {
        #     'username': '哈哈哈',
        #     'keys': '对对对'
        # }
        'books':
            (
                '鲁班七号',
                '程咬金',
                '大猪头'
            )
    }
    return render(request, 'index.html', context=context)


def book(request, book_id, book_idd):
    text = "你的书ID:" + book_id + book_idd
    return HttpResponse(text)


def author_detail(request):
    # author_id = request.GET['id']
    author_id = request.GET.get('id')
    text = 'id:%s' % author_id
    return HttpResponse(text)
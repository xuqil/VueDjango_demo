from django.shortcuts import render, HttpResponse
from sqlalchemy.ext.declarative import declarative_base
from .models import Students, Scores, Courses, Teachers
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/django_db1', encoding='utf8')
DBSession = sessionmaker(bind=engine)
session = DBSession()


def check_avg_score(request):
    students = session.query(Students.student_id, func.avg(Scores.number).label('avg')).\
        join(Scores, Students.student_id == Scores.student_id).\
        group_by(Students.student_id).having(func.avg(Scores.number) > 60)
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_students_detail(request):
    pass
    return HttpResponse("OK")


def check_teachers_number(request):
    pass
    return HttpResponse("OK")


def check_student_no_done(request):
    pass
    return HttpResponse("ok")


def check_student_done(request):
    pass
    return HttpResponse("OK")


def check_student_huang(request):
    pass
    return HttpResponse("ok")


def check_student_score_last(request):
    pass
    return HttpResponse("OK")


def check_student_all_no_done(request):
    pass
    return HttpResponse("OK")


def check_score_avg(request):
    pass
    return HttpResponse("OK")


def check_all_scores(request):
    pass
    return HttpResponse("OK")


def check_course_avg(request):
    pass
    return HttpResponse("Ok")


def check_sex_total(request):
    pass
    return HttpResponse("Ok")


def add_score(request):
    pass
    return HttpResponse('ok')


def check_fail_students(request):
    pass
    return HttpResponse("OK")


def check_number(request):
    pass
    return HttpResponse("ok")

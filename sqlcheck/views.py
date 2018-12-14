from django.shortcuts import render, HttpResponse
from sqlalchemy.ext.declarative import declarative_base
from .models import Students, Scores, Courses, Teachers
from sqlalchemy import create_engine, func, and_, or_
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
    students = session.query(Students.student_id, Students.name,
                             func.count(Courses.course_id).label('num'),
                             func.sum(Scores.number).label('sum'))\
        .join(Scores, Students.student_id == Scores.student_id)\
        .join(Courses, Scores.course_id == Courses.course_id).group_by(Students.student_id)
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_teachers_number(request):
    teacher_number = session.query(Teachers).filter(Teachers.name.like('李%')).count()
    print(teacher_number)
    return HttpResponse("OK")


def check_student_no_done(request):
    students = session.query(Scores.student_id).join(Courses, Scores.course_id == Courses.course_id)\
        .join(Teachers, Courses.teacher_id == Teachers.teacher_id).filter(Teachers.name == '黄老师')
    students = session.query(Students.student_id, Students.name).filter(~Students.student_id.in_(students))
    for student in students:
        print(student)
    return HttpResponse("ok")


def check_student_done(request):
    students = session.query(Students.student_id, Students.name).filter(Scores.student_id == Students.student_id) \
            .filter(or_(Scores.course_id == 1, Scores.course_id == 2))
    print(students)
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_student_huang(request):
    students = session.query(Scores.student_id).join(Courses, Scores.course_id == Courses.course_id)\
        .join(Teachers, Courses.teacher_id == Teachers.teacher_id).filter(Teachers.name == '黄老师')
    students = session.query(Students.student_id, Students.name).filter(Students.student_id.in_(students))
    for student in students:
        print(student)
    return HttpResponse("ok")


def check_student_score_last(request):
    s = session.query(Scores.student_id).filter(Scores.number > 60.0)
    students = session.query(Students.student_id, Students.name).filter(~Students.student_id.in_(s))
    for student in students:
        print(student)
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

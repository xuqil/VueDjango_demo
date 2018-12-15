from django.shortcuts import render, HttpResponse
from sqlalchemy.ext.declarative import declarative_base
from .models import Students, Scores, Courses, Teachers
from sqlalchemy import create_engine, func, and_, or_, desc
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
    all_num = session.query(Courses).count()
    students = session.query(Students.student_id, Students.name).join(Scores, Students.student_id == Scores.student_id)\
        .group_by(Students.student_id).having(func.count(Scores.course_id) < all_num).all()
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_score_avg(request):
    students = session.query(Students.name, func.avg(Scores.number).label('avg')). \
            join(Scores, Students.student_id == Scores.student_id)\
            .group_by(Students.student_id).order_by(desc('avg')).all()
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_all_scores(request):
    students = session.query(Courses.course_id,
                             Courses.name, func.max(Scores.number).label('max'),
                             func.min(Scores.number).label('min'))\
        .join(Scores, Courses.course_id == Scores.course_id)\
        .group_by(Courses.course_id)
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_course_avg(request):
    students = session.query(Courses.name, func.avg(Scores.number).label('avg')) \
            .join(Scores, Courses.course_id == Scores.course_id)\
            .group_by(Courses.course_id).order_by('avg')
    for student in students:
        print(student)
    return HttpResponse("Ok")


def check_sex_total(request):
    man = session.query(Students).filter(Students.gender == 1).count()
    print('男生人数：' + str(man))
    woman = session.query(Students).filter(Students.gender == 2).count()
    print('女生人数：' + str(woman))
    return HttpResponse("Ok")


def add_score(request):
    teacher = session.query(Scores) \
            .join(Courses, Scores.course_id == Courses.course_id)\
            .join(Teachers, Courses.teacher_id == Teachers.teacher_id).filter(Teachers.name == '黄老师')
    for i in teacher:
        i.number += 5
        print(i.number)
        session.query(Scores).filter(Scores.scores_id == i.scores_id).update({'number': i.number})
    session.commit()
    return HttpResponse('ok')


def check_fail_students(request):
    num = session.query(Students.student_id, Students.name,
                        func.count(Scores.course_id).label('num'))\
        .join(Scores, Students.student_id == Scores.student_id).filter(Scores.number < 60)\
        .group_by(Students.student_id).having(func.count(Scores.number < 60) >= 2)
    print(num)
    for i in num:
        print(i)
    return HttpResponse("OK")


def check_number(request):
    num = session.query(Courses.name, func.count(Scores.student_id).label('num')) \
        .join(Scores, Courses.course_id == Scores.course_id).group_by(Courses.course_id) \
        .order_by('num')
    for i in num:
        print(i)
    return HttpResponse("ok")

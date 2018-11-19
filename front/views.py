from django.shortcuts import render, HttpResponse
from .models import Student, Course, Teacher, Score
from django.db.models import Avg, Count, Sum


def check_avg_score(request):
    avg_score = Student.objects.annotate(avg=Avg("score__number")).filter(avg__gte=60).values("id", "avg")
    for row in avg_score:
        print(row)
    return HttpResponse("OK")


def check_students_detail(request):
    students = Student.objects.annotate(count=Count('score__course'), total_score=Sum("score__number")).values(
        "id", "name", "count", "score"
    )
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_teachers_number(request):
    teachers_number = Teacher.objects.all().filter(name__startswith="李").count()
    print(teachers_number)
    return HttpResponse("OK")


def check_student_no_done(request):
    students = Student.objects.exclude(score__course__teacher__name="李老师").values("id", "name")
    for student in  students:
        print(student)
    return HttpResponse("ok")


def check_student_done(request):
    students = Student.objects.filter(score__course__id__in=[1, 2]).distinct().values('id', 'name')
    for student in students:
        print(student)
    return HttpResponse("OK")

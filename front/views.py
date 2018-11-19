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
    pass


def check_student_no_done(request):
    pass


def check_student_done(request):
    pass

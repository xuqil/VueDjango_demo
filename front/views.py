from django.shortcuts import render, HttpResponse
from .models import Student, Course, Teacher, Score
from django.db.models import Avg, Count, Sum, F, Max, Min, Q


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
    for student in students:
        print(student)
    return HttpResponse("ok")


def check_student_done(request):
    students = Student.objects.filter(score__course__id__in=[1, 2]).distinct().values('id', 'name')
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_student_huang(request):
    course = Course.objects.filter(teacher__name="黄老师")
    students = Student.objects.filter(score__course__in=course).distinct().values('id', 'name')
    for s in students:
        print(s)
    return HttpResponse("ok")


def check_student_score_last(request):
    students = Student.objects.exclude(score__number__gt=60).values('id', 'name')
    for s in students:
        print(s)
    return HttpResponse("OK")


def check_student_all_no_done(request):
    students = Student.objects.annotate(num=Count(F('score__course'))).filter(num__lt=Course.objects.count()).values(
        'id', 'name'
    )
    for s in students:
        print(s)
    print(Course.objects.count())
    return HttpResponse("OK")


def check_score_avg(request):
    students = Student.objects.annotate(avg=Avg("score__number")).values('name', 'avg').distinct().order_by("-avg")
    for student in students:
        print(student)
    return HttpResponse("OK")


def check_all_scores(request):
    courses = Course.objects.annotate(min=Min("score__number"), max=Max("score__number")).values(
        'pk', 'name', 'min', 'max'
    )
    for course in courses:
        print(course)
    return HttpResponse("OK")


def check_course_avg(request):
    course_avg = Course.objects.annotate(avg=Avg("score__number")).values('name', 'avg').order_by("avg")
    for course in course_avg:
        print(course)
    return HttpResponse("Ok")


def check_sex_total(request):
    sex1_total = Student.objects.filter(gender=1).count()
    sex2_total = Student.objects.filter(gender=2).count()
    print("男生:"+str(sex1_total), "女生:"+str(sex2_total))
    return HttpResponse("Ok")


def add_score(request):
    results = Score.objects.filter(course__teacher__name="黄老师").update(number=F("number")+5)
    print(results)
    return HttpResponse('ok')


def check_fail_students(request):
    # score_number = Score
    students = Student.objects.annotate(bad_count=Count("score__number", filter=Q(score__number__lt=60))).filter(
        bad_count__gte=2).values('id', 'name', 'bad_count')
    for student in students:
        print(student)
    return HttpResponse("OK")

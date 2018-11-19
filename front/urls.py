from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('check_avg_score/', views.check_avg_score, name='check_avg_score'),
    path('check_students_detail/', views.check_students_detail, name='check_students_detail'),
    path('check_teachers_number/', views.check_teachers_number, name='check_teachers_number'),
    path('check_student_no_done/', views.check_student_no_done, name='check_student_no_done'),
    path('check_student_done/', views.check_student_done, name='check_student_done'),
    path('check_student_huang/', views.check_student_huang, name='check_student_huang'),
    path('check_student_score_last/', views.check_student_score_last, name='check_student_score_last'),
    path('check_student_all_no_done/', views.check_student_all_no_done, name='check_student_all_no_done'),
]

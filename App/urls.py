from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('teachers', views.teachers, name='teachers'),
    path('shedules', views.shedules, name='shedules'),
    path('courses', views.cours, name='courses'),
    path('classrooms', views.salles, name='classrooms'),
    path('helps', views.aides, name='helps'),
]

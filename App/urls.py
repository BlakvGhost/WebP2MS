from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('teachers-staff', views.teachers, name='teachers'),
    path('shedules', views.shedules, name='shedules'),
    path('courses', views.cours, name='courses'),
    path('classrooms', views.salles, name='classrooms'),
    path('levels', views.levels, name='levels'),
    path('helps', views.aides, name='helps'),
    
    #Ajax routes
    
    path('ajax-delete', views.ajax_delete, name='ajax.user.delete'),
]

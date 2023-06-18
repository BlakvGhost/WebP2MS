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
    path('user/profile', views.profile, name='profile'),
    
    #Ajax routes
    
    path('ajax-delete', views.ajax_delete, name='ajax.user.delete'),
    path('update-user-details', views.update_user, name='ajax.user.update'),
]

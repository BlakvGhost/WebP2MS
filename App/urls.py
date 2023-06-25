from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('gestion/les-enseignants-et-collaborateurs', views.teachers, name='teachers'),
    path('gestion/les-emplois-temps', views.shedules, name='shedules'),
    path('gestion/les-matieres', views.cours, name='courses'),
    path('gestion/les-salles-de-cours', views.salles, name='classrooms'),
    path('gestion/les-niveaux', views.levels, name='levels'),
    path('vous/vos-notifications', views.notifications, name='notifications'),
    path('vous/vos-notifications/<int:pk>', views.mark_notification, name='notifications.mark'),
    path('cendre-d-aides', views.aides, name='helps'),
    path('vous/votre-profile', views.profile, name='profile'),
    
    #Ajax routes
    
    path('ajax-delete', views.ajax_delete, name='ajax.user.delete'),
    path('update-user-details', views.update_user, name='ajax.user.update'),
    path('set-shedules', views.ajax_set_shedule, name='ajax.shedules.add'),
    path('get-shedules', views.ajax_get_shedules, name='ajax.shedules.get'),
    path('set-shedules/<int:pk>', views.ajax_set_shedule, name='ajax.shedules.update'),
    path('del-shedules', views.ajax_del_shedule, name='ajax.shedules.destroy'),
    path('check-shedules-availability', views.ajax_check_shedule, name='ajax.shedules.check'),
    path('notifications', views.get_all_notifications, name='ajax.notifications.get'),
]

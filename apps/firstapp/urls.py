from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),    
    url(r'^logout$', views.logout),
    url(r'^addAppointment$', views.addAppointment),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^updateAppointment/(?P<id>\d+)$', views.updateAppointment)
]

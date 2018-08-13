from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index, name='my_index'),
    url(r'^users/new$', views.new, name='my_new'),
    url(r'^users/(?P<id>\d+)$', views.show, name='my_show'),
    url(r'^users/(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy, name='my_destroy'),
    url(r'^users/create$', views.create),
    url(r'^users/update$', views.update, name='my_update'),
]
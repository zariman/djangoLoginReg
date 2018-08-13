from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wall, name='wall'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^/message$', views.message, name='message'),
    url(r'^/comment$', views.comment, name='comment'),
    url(r'^/delete$', views.delete, name='delete'),
    #url(r'^users/(?P<id>\d+)/destroy$', views.destroy, name='my_destroy'),
]
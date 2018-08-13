from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^register$', views.index),
    url(r'^login$', views.index, name="my_login"),
    url(r'^(?P<id>\d+)/success$', views.index, name="my_success"),
]
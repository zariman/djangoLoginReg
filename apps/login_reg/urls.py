from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="my_index"),
    url(r'^register$', views.register, name="my_register"),
    url(r'^login$', views.login, name="my_login"),
]
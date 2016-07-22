
from django.conf.urls import url, include
from django.contrib import admin
from bsdemp import views

app_name = "bsdemp"

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^(?P<employee_id>[0-9]+)$', views.detail, name="detail"),
]

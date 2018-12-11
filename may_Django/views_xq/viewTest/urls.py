from django.conf.urls import url
# from django.contrib import admin
from viewTest import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^show_arg/(?P<id1>\d+)/',views.show_arg),
    url(r'^show_method/',views.show_method),
    url(r'^show_reqarg/',views.show_reqarg),
    url(r'^json1/',views.json1),
    url(r'^json2/', views.json2),
    url(r'^login/',  views.login),
    url(r'^verfiy/', views.verfiy),
    url(r'^red1/', views.red1),
    url(r'^set_cke/', views.set_cke),
    url(r'^get_cke/', views.get_cke),
    url(r'^set_ses/', views.set_ses),
    url(r'^get_ses/', views.get_ses),

]
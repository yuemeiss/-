"""testspider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from spiderapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^qiushi/$', views.QiushiList.as_view()),
    url(r'^qiushi/(?P<pk>[0-9]+)/$', views.QiushiDetail.as_view()),

    url(r'^juzicon/$', views.juziconList.as_view()),
    url(r'^juzicon/(?P<pk>[0-9]+)/$', views.juziconDetail.as_view()),

    url(r'^juzitag/$', views.juzitagList.as_view()),
    url(r'^juzitag/(?P<pk>[0-9]+)/$', views.juzitagDetail.as_view()),

    # 调出API登录
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^playapp/$',views.myapptest)

]

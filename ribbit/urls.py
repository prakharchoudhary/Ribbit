"""ribbit URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from ribbit_app import views as rviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rviews.index), # root
    url(r'^login$', rviews.login_view), # login
    url(r'^logout$', rviews.logout_view), # logout
    url(r'^signup$', rviews.signup), # signup
    url(r'^ribbits$', rviews.public), #public ribbits
    url(r'^submit$', rviews.submit), # submit
    url(r'^users$', rviews.users),
    url(r'^users/(?P<username>\w{0,30})/$', rviews.users),
    url(r'^follow$', rviews.follow),
]

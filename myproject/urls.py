"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage', views.mypage, name='home'),
    path('mypage2', views.mypage2, name='home'),
    path('addno', views.addNo, name='home'),
    path('regform', views.regform, name='home'),
    path('select', views.selectform, name='home'),
    path('reg', views.registration, name='home'),
    path('login', views.login, name='home'),
    path('users', views.users, name='home'),
    path('adminpage', views.admin, name='home'),
    path('delete', views.delete, name='home')



]+staticfiles_urlpatterns()

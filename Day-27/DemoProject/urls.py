"""DemoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from SampleApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/',views.sa),
    path('y/<str:p>/',views.printname),
    path('k/<int:a>/<str:n>/',views.stdtls),
    path('p/<str:ename>/<str:epid>/<int:eage>/',views.empdtls),
    path('m/<str:stname>/<str:sid>/',views.stprint),
    path('nk/<str:ename>/',views.eprint),
    path('km/<str:sname>/<int:y>/',views.jprint),
    path('j/',views.gy),
    path('q/',views.vb),
    path('k/',views.idt),
    path('mn/',views.dy),
    path('kl/',views.btp,name="hm"),
    path('ab/',views.about,name="abt"),
    path('cnt/',views.contact,name="ct"),
    path('reg/',views.register,name="rg"),
    path('yu/',views.index,name="indx"),
    path('stp/<int:w>/',views.stupdate,name="stup"),
    path('stdt/<int:y>/',views.stdel,name="std"),
    path('',views.home,name="hme"),
    path('abt/',views.abou,name="abtt"),
]

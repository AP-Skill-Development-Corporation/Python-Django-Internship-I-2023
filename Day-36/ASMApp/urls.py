from django.urls import path
from ASMApp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('ab/',views.about,name="abt"),
	path('ct/',views.contact,name="cnt"),
	path('reg/',views.register,name="rg"),
	path('lgo/',ad.LoginView.as_view(template_name='html/login.html'),name="lg"),
	path('lgot/',ad.LogoutView.as_view(template_name='html/logout.html'),name="lgto"),
]
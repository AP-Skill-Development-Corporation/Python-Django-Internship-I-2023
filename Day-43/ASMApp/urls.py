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
	path('pfe/',views.profile,name="pf"),
	path('upf/',views.updpf,name="upfe"),
	path('tasgn/',views.tsgnlist,name="taslist"),
	path('tas/<int:v>/',views.astup,name="atup"),
	path('tchdl/<int:g>/',views.adlt,name="atdh"),
	path('stlist/',views.staslist,name="stas"),
	path('ast/<int:h>/',views.astt,name="asty"),
	path('ssblst/',views.stsblst,name="ssblt"),
	path('sbup/<int:t>/',views.ssbup,name="supd"),
	path('ssub/<int:m>/',views.ssubf,name="ssb"),
	path('tst/',views.tstup,name="tstp"),
	path('tstmr/<int:p>/',views.tsmrup,name="tsmr"),
	path('adlist/',views.adlistv,name="adls"),
	path('adup/<int:j>/',views.adups,name="adsup"),
]
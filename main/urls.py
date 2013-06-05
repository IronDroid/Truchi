from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^configuracion/$', 'configuracion', name='config'),
    url(r'^home/$', 'home', name='home'),
    url(r'^perfil/$', 'perfil', name='perfil'),
    url(r'^horario/$', 'horario', name='horario'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^generador/$', 'generador', name='generador'),
)
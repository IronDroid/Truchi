from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^configuracion/$', 'main.views.configuracion', name='config'),
    url(r'^home/$', 'main.views.home', name='home'),
    url(r'^perfil/$', 'main.views.perfil', name='perfil'),
    url(r'^horario/$', 'main.views.horario', name='horario'),
    url(r'^logout/$', 'main.views.logout', name='logout'),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'', include('social_auth.urls')),
)

urlpatterns += staticfiles_urlpatterns()
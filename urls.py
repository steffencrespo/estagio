from django.conf.urls.defaults import *
from estagio.pizza import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^estagio/', include('estagio.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
    (r'^termo/create/', views.cria_termo),
	(r'^termo/list/', views.avalia_termo),
	(r'^termo/edit/(?P<codigo_termo>[\d]+)/', views.edita_termo),
	(r'^empresa/cadastro', views.cadastra_empresa),
    url(r'^login/', views.autenticacao, name="login"),
    url(r'^logout/', views.deslogar, name="logout"),
    (r'^sistemaestagios/', views.welcome_page),
)

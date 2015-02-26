from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings


from django.contrib import admin
#from my.forms import AuthenticationForm
admin.autodiscover()
#admin.site.login_form = AuthenticationForm


urlpatterns = patterns('',

      
     url(r'^$', 'guru.core.views.home', name='home'),

     url(r'^$', 'guru.core.views.home_training', name='home_training'),
    
     url(r'^treinamentos/$', 'guru.core.views.treinamento', name='treinamentos'),
    
     url(r'^treinamentos_plataforma/$', 'guru.core.views.treinamentos_plataforma', name='treinamentos_plataforma'),
    
     url(r'^treinamentos_produto/$', 'guru.core.views.treinamentos_produto', name='treinamentos_produto'),
     
     url(r'^treinamentos/(?P<slug>[\w-]+)', 'guru.core.views.modulos', name='modulos'),

     url(r'^treinamentos/(?P<slug>[\w-]+)', 'guru.core.views.voltar_modulo', name='voltar_modulo'),
     
     url(r'^modulos/(?P<slug>[\w-]+)','guru.core.views.etapas', name='etapas'),

     url(r'^etapas/(?P<id>\d+)$', 'guru.core.views.video', name='video'),

     url(r'^globotreinamentos/$', 'guru.core.views.aovivo', name='aovivo'),

     url(r'^globotreinamentos/(?P<slug>[\w-]+)', 'guru.core.views.videovivo', name='videovivo'),

     url(r'^novidades/(?P<slug>[\w-]+)', 'guru.core.views.novidades', name='novidades'),

     url(r'^ondemand/(?P<slug>[\w-]+)', 'guru.core.views.ondemand', name='ondemand'),

     url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login2.html'}),
     
     url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name': 'logout.html'}), 

     url(r'^treinamentos/(?P<slug>[\w-]+)', 'guru.core.views.voltar', name='voltar'),

     url(r'^admin/', include(admin.site.urls)),







) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




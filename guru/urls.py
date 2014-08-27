from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     
     url(r'^$', 'guru.core.views.home', name='home'),

     url(r'^$', 'guru.core.views.home_training', name='home_training'),
    
     url(r'^treinamentos/$', 'guru.core.views.treinamento', name='treinamentos'),
    
     url(r'^treinamentos_plataforma/$', 'guru.core.views.treinamentos_plataforma', name='treinamentos_plataforma'),
    
     url(r'^treinamentos_produto/$', 'guru.core.views.treinamentos_produto', name='treinamentos_produto'),
     
     url(r'^treinamentos/(?P<slug>[\w-]+)', 'guru.core.views.modulos', name='modulos'),
     
     url(r'^modulos/(?P<slug>[\w-]+)', 'guru.core.views.etapas', name='etapas'),

     url(r'^etapas/(?P<id>\d+)$', 'guru.core.views.video', name='video'),

     url(r'^play/$', 'guru.core.views.aovivo', name='aovivo'),

     url(r'^play/(?P<slug>[\w-]+)', 'guru.core.views.videovivo', name='videovivo'),

    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include(admin.site.urls)),



)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from embed_video.fields import EmbedVideoField


# retorno para status 
STATUS_CHOICES = (
    ('d', 'Rascunho'),
    ('p', 'Publicado'),    
)
# retorno para status 
STATUS_SEGMENT = (
    ('p', 'Plataforma'),
    ('pr', 'Produto'), 
    ('av', 'ao vivo')   
)

def foo(instance, filename):
    return "%s/%s"% (instance.icon,filename)


# Classe abstrata     
class Usual(models.Model):
    time = models.DateTimeField(auto_now_add= True)
    name = models.CharField(_('titulo'),max_length=100)
    description = models.TextField(_('descricao'),max_length=100,blank=True)
    icon = models.ImageField(_('icone:'),null=True, blank=True, upload_to= 'staticfiles')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    
    class Meta:
        abstract = True
                  
# Classe de treinamento ( herdeira de classe abstrata )
class Training(Usual):
    segment = models.CharField(max_length=2,choices=STATUS_SEGMENT)
    video = EmbedVideoField(blank=True)
    slug = models.SlugField()


    class Meta:
        verbose_name = _('Treinamento')
        verbose_name_plural = _('Treinamentos')

    def __unicode__(self):
        return (self.name)

#Classe de modulos ( herdeira de classe abstrata,com chave estrangeira de treinamento )
class Modulo(Usual):
	  trainings = models.ForeignKey('Training',verbose_name=_('Treinamento'))
          slug = models.SlugField()
	  video = EmbedVideoField(blank=True)  # same like models.URLField()
	  position = models.PositiveSmallIntegerField ("Position", blank=True,null=True)
    
          def __unicode__(self): 
             return (self.name)    

#Classe de etapas ( herdeira de classe abstrata,com chave estrangeira de modulo )
class Step(Usual):
    modulos = models.ForeignKey('Modulo',verbose_name=_('Modulos'))
    slug = models.SlugField()
    video = models.URLField(max_length=200,null=True, blank=True)
    position = models.PositiveSmallIntegerField ("Position",blank=True,null=True)
    
    class Meta:
        verbose_name = _('Etapa')
        verbose_name_plural = _('Etapas')
        ordering = ['position']
        
    def __unicode__(self):
        return self.name    

    
    

	







# Create your models here.

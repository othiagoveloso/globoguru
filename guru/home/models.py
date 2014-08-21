from django.db import models
from django.utils.translation import ugettext_lazy as _
from embed_video.fields import EmbedVideoField


STATUS_CHOICES = (
    ('d', 'Rascunho'),
    ('p', 'Publicado'),    
)
# Modelos do sistema didata
class Spotlight(models.Model):
        video = EmbedVideoField(blank=True)
        title=models.TextField(_('titulo'),max_length=100,blank=True)
        subtitle=models.TextField(_('subtitulo'),max_length=100,blank=True)
        status = models.CharField(max_length=1, choices=STATUS_CHOICES) 
        
         
        class Meta:
            verbose_name = _('Destaque')
            verbose_name_plural = _('Destaques')

        def __unicode__(self):
            return (self.title)

class Carousel(models.Model):
    title=models.CharField(_('titulo'),max_length=100,)
    image = models.ImageField(_('icone:'),null=True, blank=True, upload_to= 'icones/img')            
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)   
     
    class Meta:
            verbose_name = _('Carrossel')
            verbose_name_plural = _('Carrossel')

    def __unicode__(self):
            return (self.title)        




# Create your models here.

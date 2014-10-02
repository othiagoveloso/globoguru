from django.contrib import admin
from guru.home.models import Spotlight, Carousel


class SpotlightAdmin(admin.ModelAdmin):

    list_display = ('title', 'subtitle','status','video')
    list_editable =( 'status',)
    fields = ('status','title', 'subtitle','video',)
    
    
admin.site.register(Spotlight, SpotlightAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title','image','status',)

admin.site.register(Carousel, CarouselAdmin)    


# Register your models here.

# Register your models here.

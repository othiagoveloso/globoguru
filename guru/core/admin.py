from django.contrib import admin
#from django_admin_bootstrapped.admin.models import SortableInline
from guru.core.models import Training, Modulo, Step

from django_admin_bootstrapped.admin.models import SortableInline






#visualizando o treinamento no admin

def published(modeladmin, request, queryset):
    queryset.update(status='p')
    published.short_description = "publicar"

class StepSort(admin.StackedInline, SortableInline):
    model = Step
    extra = 0


class TrainingAdmin(admin.ModelAdmin):

    
    list_display = ('name','segment','video', 'status','time','description')
    prepopulated_fields = {'slug': ('name',)}
    
    list_editable = ('segment' ,'status',)
    search_fields = ('name',  'icon',)
    fields = ('name','slug','description','icon','video','segment','status')
    actions = [published]
    
    
admin.site.register(Training, TrainingAdmin)

#visualizando o modulo no admin
class ModuloAdmin(admin.ModelAdmin):

    list_display = ( 'name', 'trainings','video','status', 'position')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('status',)
    search_fields = ('trainings', 'name' )
    list_filter=('trainings', 'name')
    fields = ('name','slug', 'trainings', 'description', 'icon', 'video','status','position')
    actions = [published]		
    
    
		

admin.site.register(Modulo, ModuloAdmin)

#class Ste(admin.StackedInline, SortableInline):
    #model = Step
    #extra = 0

#visualizando a etapa no admin
class StepAdmin(admin.ModelAdmin):


    list_display = ('name', 'modulos', 'video','status','position')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('position', 'status')
    search_fields = ('modulos', 'name', 'description', 'icon', 'video')
    list_filter=('modulos', 'name')
    ordering = ('position',)
    fields = ('name','slug', 'modulos', 'description', 'icon', 'video','status','position')
   
   


admin.site.register(Step, StepAdmin)

class HomeAdmin(admin.ModelAdmin):
    list_display = ('spotlight_title')


#admin.site.register(Home, HomeAdmin)






# Register your models here.

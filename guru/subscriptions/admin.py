from django.contrib import admin
from guru.subscriptions.models import Subscription



class SubscriptionAdmin(admin.ModelAdmin):

    
    list_display = ('name','username','password')
    
    fields = ('name','username','password')
   
    
    
admin.site.register(Subscription, SubscriptionAdmin)

# Register your models here.

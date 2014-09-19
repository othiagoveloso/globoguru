from django import forms
from guru.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    
    class meta:
    	model = Subscription
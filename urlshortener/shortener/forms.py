from django import forms
from .models import UrlPair

class NewUrlForm(forms.ModelForm):
    class Meta:
        model = UrlPair
        fields = ['long_url']
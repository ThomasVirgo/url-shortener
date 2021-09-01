from django import forms
from .models import UrlPair


class NewUrlForm(forms.ModelForm):
    class Meta:
        model = UrlPair
        fields = ['long_url']

    def __init__(self, *args, **kwargs):
        super(NewUrlForm, self).__init__(*args, **kwargs)
        self.fields['long_url'].label = "Enter URL Here:"

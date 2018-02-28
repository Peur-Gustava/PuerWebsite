from django import forms
from . models import file_upload

class Uploadform(forms.ModelForm):
    class Meta:
       model = file_upload
       fields = '__all__'

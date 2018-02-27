from django import forms
from django.forms import ModelForm
from . models import *

class Uploadform(forms.ModelForm):
    class Meta:
       model = file_upload
       fields = '__all__'

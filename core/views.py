from django.shortcuts import render
from .models import *
from .forms import *

def FileUpload(request):
    form = Uploadform()
    if request.method == 'POST':
        form = Uploadform(request.POST)
        if form.is_valid():

            form.save()
    else:
            form = Uploadform()

    return render(request,'file_upload.html',{'form':Uploadform() })

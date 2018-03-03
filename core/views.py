from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *

@login_required
def FileUpload(request):
    form = Uploadform()
    if request.method == 'POST':
        form = Uploadform(request.POST,request.FILES)
        if form.is_valid():
            # print(form.proof)
            form.save()
        else:
            form = Uploadform()
    return render(request,'file_upload.html',{'form':form })

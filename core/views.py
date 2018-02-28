from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *

# @login_required
def FileUpload(request):
    form = Uploadform()
    if request.method == 'POST':
        form = Uploadform(request.POST)
        if form.is_valid():
            print(form.proof)
            newfile = form.save(commit=False)
            doc = form.cleaned_data['proof']
            print(doc)
            print("Hello")
            newfile.proof = doc
            print(newfile.proof)
            newfile.save()
        else:
            form = Uploadform()
    return render(request,'file_upload.html',{'form':Uploadform() })

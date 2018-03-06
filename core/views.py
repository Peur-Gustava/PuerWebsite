from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from .tasks import add

# add.delay(2,2)
# core.tasks.add(2, 2)


@login_required
def FileUpload(request):
    form = Uploadform()
    if request.method == 'POST':
        form = Uploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()

        else:
            form = Uploadform(commited=False)
            data = form.cleaned_data

            seriousmlprocess(data)
    return render(request,'file_upload.html',{'form':form })

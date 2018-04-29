from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import *
from .forms import *



class Learnsomethingnew(LoginRequiredMixin,TemplateView):
    template_name = 'core/learnsomethingnew.html'

class aboutus(TemplateView):
    template_name = 'core/aboutus.html'

class SaferInternet(TemplateView):
    template_name = 'core/saferinternet.html'

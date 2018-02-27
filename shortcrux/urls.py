from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/$',views.FileUpload,name="upload"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]

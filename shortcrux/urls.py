from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core.views import Learnsomethingnew,aboutus,SaferInternet
from login import views as login_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$',login_view.Signup,name='signup'),
    url(r'^$',SaferInternet.as_view(),name='SaferInternet'),
    url(r'^aboutus/$',aboutus.as_view(),name='contactus'),
    url(r'^learnsomethingnew/$',Learnsomethingnew.as_view(),name='Learnsomethingnew'),
]

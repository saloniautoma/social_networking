from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

app_name = 'account'
urlpatterns = [
        url(r'^login/$', login, {'template_name': 'login.html'} ,name='login'),
        url(r'^logout/$', logout, {'template_name':'logout.html'}, name='logout'),
        url(r'^register/$', views.register, name='register'),
        url(r'^user_list/$', views.UserList.as_view(), name='user_list'),
        url(r'^$', views.ahome, name='home'),
        url(r'^login/$', login, {'template_name': 'login.html'} ,name='login'),
        url(r'^logout/$', logout, {'template_name':'logout.html'}, name='logout'),
        url(r'^register/$', views.register, name='register'),
        url(r'^userlist/$', views.UserList.as_view(), name='userlist'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
        url(r'^(?P<id>\d+)/',views.deleteprofile, name='delete'),
        url(r'^profile/changepassword/$', views.changepassword, name='change_password'),
        url(r'^profile/(?P<id>\d+)/',views.userdetail, name='user_detail'),


]

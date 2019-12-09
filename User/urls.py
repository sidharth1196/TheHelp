from . import views
from django.conf.urls import url
from django.urls import path
from Home.models import Work

app_name = 'User'

urlpatterns = [
    #url(r'^$', views.index, name='index')
    #url(r'^$', ListView.as_view(queryset=Work.objects.all(), template_name="Home/home.html"))
    path('work/<int:work_id>', views.workers, name='workers'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    path('userprofile/<int:profile_id>', views.userprofile_info, name='userprofile_info'),
    path('save_userprofile/<int:profile_id>', views.save_userprofile, name='save_userprofile'),
    url(r'^user_login/workerprofile/(\d+)', views.workerprofile, name='workerprofile'),
    path('save_workerprofile/<int:profile_id>', views.save_workerprofile, name='save_workerprofile'),
]

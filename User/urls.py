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
]

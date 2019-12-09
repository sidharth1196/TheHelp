from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView

app_name = 'Home'

urlpatterns = [
    url(r'^$', views.index, name='index')
    #url(r'^$', ListView.as_view(queryset=Work.objects.all(), template_name="Home/home.html"))
]

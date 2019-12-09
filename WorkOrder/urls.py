from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('quote/<int:worker_id>/<int:userprofile_id>', views.create_quote, name='create_quote'),
    path('confirm/<int:worker_id>/<int:quote_id>', views.confirm_booking, name='confirm_booking'),
    path('completion/<int:worker_id>/<int:order_id>', views.completion, name='completion')
]
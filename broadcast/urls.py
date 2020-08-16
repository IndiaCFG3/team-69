from . import views
from django.conf.urls import url

urlpatterns = [ 
    url(r'broadcast$', views.broadcast_sms, name="default"),
]
from . import views
from django.conf.urls import url

urlpatterns = [ 
    url('broadcast', views.broadcast_sms, name="signup-sms"),
]
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('signup/', 		core_views.register,													name='signup'),
    path('login/', 			auth_views.LoginView.as_view(template_name = 'user/login.html'),		name='login'),
   	path('logout/', 		auth_views.LogoutView.as_view(template_name = 'user/logout.html'),		name='logout'),
   	path('profile/', 		core_views.profileview,													name='profile'),
    path('profile/update/', core_views.profileupdate,												name='profile-update'),
]

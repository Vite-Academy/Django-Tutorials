from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *

urlpatterns = [
    # ... other URL patterns
    # path('accounts/', include('accounts.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),
]

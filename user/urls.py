from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView,RegisterView ,LogoutView,profile,profile_view
from .forms import  LoginForm

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',authentication_form=LoginForm), name='login'),
    path('logout/',LogoutView,name='logout'),
    path('profile/', profile, name='users-profile'),
    path('profile_view/', profile_view, name='users-profile_view'),
    
]
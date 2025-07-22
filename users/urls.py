from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from .views import logged_out_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='logged_out'), name='logout'),
    path('logged-out/', logged_out_view, name='logged_out'), 
    path('profile/', views.profile_view, name='profile'),
]
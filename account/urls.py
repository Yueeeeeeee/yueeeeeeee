from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'
urlpatterns = [
    # post views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
        name='password_change'
        ),
    path('password_changed/',
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_changed.html'),
        name='password_changed'
        )
]
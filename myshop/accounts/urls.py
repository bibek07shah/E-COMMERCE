from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # authentication part------------------------------------------------>



    path('register/',register,name='register'),
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    
    path('profile/',profile,name='profile'),
    path('my_order/',my_order,name='my_order'),
    path('update_profile/',update_profile,name='update_profile'),
    path('change_password/',change_password,name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='change_password.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    
]

from django.urls import path

from registers import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView

app_name ='register_app'

urlpatterns = [
    path('login/',views.UserLogin.as_view(),name="login"),
    path('register/',views.SignupView.as_view(),name="register"),
    path('logout/',views.UserLogout.as_view(),name="logout"),
   
    
]





'''
for which email is sent use SMTP configuration in settings.py
https://docs.djangoproject.com/en/3.0/topics/auth/default/
Submit email form    -->PasswordResetViews.as_views()
email sent success  -->PasswordResetDoneView.as_views()
Link to password reser form in email ---user see email   -->PasswordResetConfirmView.as_views()
password sucessfully changed message and user can login using new password   -->PasswordResetCompleteView.as_views()


-------------------------------------------------------------
-->python decouple concept for email and other things secrete|
--------------------------------------------------------------
'''

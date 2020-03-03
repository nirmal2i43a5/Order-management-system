from django.urls import path

from registers import views

app_name ='register_app'

urlpatterns = [
    path('login/',views.UserLogin.as_view(),name="login"),
   path('register/',views.SignupView.as_view(),name="register"),
   path('logout/',views.UserLogout.as_view(),name="logout"),
   
    
]

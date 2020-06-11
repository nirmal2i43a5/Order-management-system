"""ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from registers import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first_page,name="first"),
    path('dashboard/',views.dashboard,name="dashboard"),
#    path('',include('django.contrib.auth.urls')),
    
    path('user/',include('registers.urls', namespace = 'register_app')),
    path('customers/',include('customers.urls', namespace="customer_app")),
    path('products/',include('products.urls', namespace="product_app")),#namespace is the app_name in products.urls
    path('orders/',include('orders.urls', namespace="order_app")),
      path('employee-profile/',TemplateView.as_view(template_name="registers/user_view.html"),name="user-profile"),
        path('admin-profile/',TemplateView.as_view(template_name="registers/admin_view.html"),name="admin-profile"),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'passwordreset/password_reset_email.html'), 
         name = "password_reset"),
    
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = 'passwordreset/password_reset_sent.html'), 
         name = "password_reset_done"),
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset/password_reset_form.html'),
         name="password_reset_confirm"),  
       
     #<token> check  for valid user or not--><uidb64> user id encoded in base 64--this email is sent to the user
     #<uidb64> helps to know user who request for password
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
         name="password_reset_complete"),
   
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




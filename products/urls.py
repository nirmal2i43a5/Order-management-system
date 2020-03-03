

from django.urls import path

from products import views

app_name = 'product_app'

urlpatterns=[
    path('create/',views.create,name='create'),
    path('list/',views.index,name='index'),    
]

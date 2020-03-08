from django.urls import path

from customers import views



app_name='customer_app'

urlpatterns=[
    path('create/',views.create,name='create'),
    path('list/',views.index,name='list'),
    path('edit/<int:cid>/',views.edit,name='edit'),#here i pass primary key
    path('delete/<int:cid>/',views.delete,name='delete'),
    path('order/<int:cid>',views.cus_ord_view,name = 'view')
    
]

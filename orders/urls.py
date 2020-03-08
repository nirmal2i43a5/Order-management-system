from django.urls import path
from orders import views

app_name = "order_app"

urlpatterns = [
    path('create/<int:cid>/', views.create, name = "create"),#I pass cid as for instance to show customer name when i click Add Order
    path('list/',views.index,name="list"),
    path('edit/<int:oid>/',views.edit,name="edit"),
    path('delete/<int:oid>/',views.delete,name="delete"),
    
]





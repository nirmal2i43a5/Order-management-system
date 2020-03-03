from django.urls import path
from orders import views

app_name = "order_app"

urlpatterns = [
    path('create/',views.create,name="create"),
    path('list/',views.index,name="list"),
    
]





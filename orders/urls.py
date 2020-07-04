from django.urls import path
from orders import views,pdfviews

app_name = "order_app"

urlpatterns = [
    path('create/<int:cid>/', views.create, name = "create"),#I pass cid as for instance to show customer name when i click Add Order
    path('list/',views.index,name="list"),
    path('pdf/',pdfviews.GeneratePDF.as_view(),name="pdf"),
    path('edit/<int:cid>/<int:oid>/',views.edit,name="edit"),
    path('search/',views.search,name="search"),
    path('delete/<int:oid>/',views.delete,name="delete"),
    
]





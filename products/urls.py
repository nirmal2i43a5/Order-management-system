

from django.urls import path

from products import views
from products import pdfviews


app_name = 'product_app'

urlpatterns=[
    path('create/',views.create, name="create"),
    path('list/',views.index, name = "list"), 
    path('search',views.search,name="search"),
    path('pdf/',pdfviews.GeneratePDF.as_view(),name="pdf"),
    path('edit/',views.edit,name="edit"),
    path('delete/',views.delete,name="delete_product"),
    path('productData/<int:cid>/',views.productData,name="product-data")
  
]

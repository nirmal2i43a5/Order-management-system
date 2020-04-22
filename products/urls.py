

from django.urls import path

from products import views
from products import pdfviews


app_name = 'product_app'

urlpatterns=[
    path('create/',views.create, name="create"),
    path('list/',views.index, name = "list"), 
    path('pdf/',pdfviews.GeneratePDF.as_view(),name="pdf"),
    path('edit/<int:pid>/',views.edit,name="edit"),
    path('delete/<int:pid>/',views.delete_product,name="delete_product"),
  
]

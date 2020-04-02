from django.urls import path

from customers import views
from customers import pdfviews,billviews



app_name='customer_app'

urlpatterns=[
    # path('create/',views.create,name='create'),
    # path('',views.CustomerPagination.as_view(),name="customer_pagination"),#it assists to show page
    path('list/',views.index,name='list'),#assists to show data
    path('edit/<int:cid>/',views.edit,name='edit'),#here i pass primary key
    path('delete/<int:cid>/',views.delete,name='delete'),
    path('order/<int:cid>',views.cus_ord_view,name = 'view'),
    path('pdf/',pdfviews.GeneratePDF.as_view(),name="pdf"),
    path('orders/bill/<int:cid>',billviews.GenerateBILL.as_view(),name="bill"),
     path('add-to-cart/<slug>/',views.add_to_cart, name='add-to-cart'),
    path('remove-single-item-from-cart/<int:cid>/',views.cus_ord_view,
         name='remove-single-item-from-cart'), 
]

from django.urls import path

from customers import views
from customers import pdfviews,billviews
from customers import exportviews



app_name='customer_app'

urlpatterns=[
    path('create/',views.create,name='create'),
    # path('',views.CustomerPagination.as_view(),name="customer_pagination"),#it assists to show page
    path('list/',views.index,name='list'),#assists to show data
    path('edit/',views.edit,name='edit'),#here i pass primary key
    path('search/',views.search,name="search"),
    path('delete/',views.delete,name="delete"),
    path('customer-id-<int:cid>/order/',views.cus_ord_view,name="view"),
    path('pdf/',pdfviews.GeneratePDF.as_view(),name="pdf"),
    path('orders/bill/<int:cid>',billviews.GenerateBILL.as_view(),name="bill"),
    path('export/',exportviews.export,name="export"),
    
]

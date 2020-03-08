from django.db import models

# Create your models here.

from customers.models import Customer
from products.models import Product

class Order(models.Model):
    status=(
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for delivery','out for delivery')
        
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)#customer_id is foreign key in tbl_orders
    '''this means if Customer is deleted then I want to set Order to NULL value in database but dont want to delete
        -if on_delete = models.CASCADE then deleting on Customer will also delete Order which is bad practice
    '''
    #Producat and Customer associated with Order
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)#maila order table Product ko dtails pauxu
    '''
    Similarly if Product is deleted then order set to Null value'''
    
    created_at=models.DateTimeField(max_length=50,null=True)
    status=models.CharField(max_length=100,null=True,choices=status)
    
    
        
        
    def __str__(self):
        return self.product.name  #w/ relationship
    
  
    
    

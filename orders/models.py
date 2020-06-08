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
    
    created_at=models.DateTimeField(max_length=50,null=True,auto_now=True)
    status=models.CharField(max_length=100,null=True,choices=status)
    quantity = models.IntegerField(default=1,blank=False)
    total_price = models.DecimalField(default=0.00,max_digits=10000,decimal_places=2)
    
    
        
        
    # def __str__(self):
    #     return self.product.name  #w/ relationship
    
    
    def get_total_item_price(self):
        return self.quantity * self.product.price
    
    
    
      # def get_total_discount_item_price(self):
    #         return self.quantity * self.product.discount_price

    # def get_amount_saved(self):
    #     return self.get_total_item_price() - self.get_total_discount_item_price()

    # def get_final_price(self):
    #     if self.product.discount_price:
    #         return self.get_total_discount_item_price()
    #     return self.get_total_item_price()
    
  
    
    

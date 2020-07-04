from django.contrib import admin

from customers.models import Customer


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    
    # def full_name(obj):
    #     return obj

    # list_display=['first_name','last_name','email','contact','created_at','status']
    list_display=['name','email','contact','date_created']
    #full_name la first name and last name lai concatenate garxa
    
    

    
'''
list_display=['status','customer','product']
if i write customer and product then i can see name of product 
and first and last name of customer in Order table in django admin UI
'''
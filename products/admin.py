from django.contrib import admin

from products.models import Product,HistConf

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display=['name','price','category','description']
    
admin.site.register(HistConf)

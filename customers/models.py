from django.db import models

# Create your models here

class Customer(models.Model):
   
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    # status=models.BooleanField()    
      
    def __str__(self):
        return self.name
    
    
          
    # def save(self,*args,**kwargs):
    #     if not self.id:
    #         self.slug=slugify(self.first_name)
    #     super(Customer,self).save(self,*args,**kwargs):





    
        

    
    
    
    
    

  
    
    
    

    
    
    
    
    
    
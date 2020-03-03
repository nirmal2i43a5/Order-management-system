from django.db import models

# Create your models here

class Customer(models.Model):
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    created_at=models.DateField(auto_now=True)
    status=models.BooleanField(default=True)    
      
    def __str__(self):
        return ('%s %s'%(self.first_name,self.last_name))
    
    
          
    # def save(self,*args,**kwargs):
    #     if not self.id:
    #         self.slug=slugify(self.first_name)
    #     super(Customer,self).save(self,*args,**kwargs):





    
        

    
    
    
    
    

  
    
    
    

    
    
    
    
    
    
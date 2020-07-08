from django.db import models

# Create your models here.

class Product(models.Model):
    
    category=(
                 ('indoor service','indoor service'),
                 ('outdoor service','outdoor service')
              )
   
    PRICE_UNITS_CHOICES = (
     #   The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name.
        ('UNIT', 'Choose Product Unit'),
        ('Kg', 'kg'),
        ('L','litre'),
        ('Pcs','pcs'),
        ('m2', 'm2'),
        ('m3', 'm3'),
        ('ml', 'ml'),
      
     
    )
    name=models.CharField(max_length=50,null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    quantity = models.IntegerField(blank=False,default=1)
    unit = models.CharField(max_length= 50,choices = PRICE_UNITS_CHOICES,default='')
    # slug = models.SlugField(max_length=80,default=False)
    category=models.CharField(max_length=200,null=True,choices=category)
    description=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now=True,null=True)
   
    def __str__(self):
        return self.name

class HistConf(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	actual= models.PositiveSmallIntegerField()#it is the actual quantity that is b4 deleting or adding 
	transition = models.IntegerField()#it is the quantity no that is added or deleted
	total = models.PositiveSmallIntegerField()#quantity remains after adding or removing 
	user = models.CharField(max_length=50)
	time = models.DateTimeField(auto_now=True,null=True)

	@classmethod
	def create(cls, actual, transition, pid, user=''):
		hist = cls(actual=actual, transition=transition, total=actual+transition, user=user, time=datetime.datetime.now(), item=pid)
		return hist

	def __str__(self):
		return f"Before: {self.actual} Change: {self.transition} After: {self.total} by user: {self.user} at {self.time}"



    
  

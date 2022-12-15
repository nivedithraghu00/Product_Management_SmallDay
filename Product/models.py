from django.db import models


# Create your models here.
class Product(models.Model):
    product_id=models.CharField(verbose_name="product_id",primary_key = True ,max_length=65)
    product_name = models.CharField(verbose_name="model_name", max_length=65)
    model_name = models.CharField(verbose_name="model_name", max_length=65)
    price = models.CharField(verbose_name="price", max_length=10)
    warranty = models.IntegerField(verbose_name="warranty")

class Batch(models.Model):
    batch_ID = models.CharField(verbose_name="Batch_ID",primary_key = True ,max_length=65)
    batch_Qty = models.IntegerField(verbose_name="Batch_qty",default=0 )
    batch_Date =  models.DateField(verbose_name="Batch_Date" )
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Inventory(models.Model):
        inventory_id =  models.CharField(verbose_name="batch_ID",max_length=65)
        product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
        batch_ID = models.ForeignKey(Batch, on_delete=models.CASCADE)
        status =models.CharField(verbose_name="Product Name", max_length=65,default="Available" )
  
    
    

from django.db import models

# Create your models here.
class Customer_Order(models.Model):
    customer_Order_id=models.CharField(verbose_name="customer_Order_id",max_length=65)
    customer_id =  models.CharField(verbose_name="customer_id",max_length=65)
    date = models.DateField()
    payment_mode = models.CharField(verbose_name="payment_mode",max_length=65)
    # dealers_inv_id =models.ForeignKey(Product, on_delete=models.CASCADE)  this should be added from dealer inventory 


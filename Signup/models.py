from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.

class EmpSignup(models.Model):
        first_name =  models.CharField(verbose_name="first_name",max_length=65)
        last_name = models.CharField(verbose_name="last_name",max_length=65)
        gender = models.CharField(verbose_name="gender",max_length=65)
        email =models.CharField(verbose_name="email",max_length=65)
        roll =models.CharField(verbose_name="roll",max_length=65,default="EMP")
        password =models.CharField(verbose_name=" password", max_length=65 )

class DealerSignup(models.Model):
        dealer_id =  models.CharField(verbose_name="first_name",max_length=65)
        first_name =  models.CharField(verbose_name="first_name",max_length=65)
        last_name = models.CharField(verbose_name="last_name",max_length=65)
        gender = models.CharField(verbose_name="gender",max_length=65)
        gst=models.CharField(verbose_name="gst",max_length=65)
        dealer_type =models.CharField(verbose_name="dealer_type",max_length=65)
        email =models.CharField(verbose_name="email",max_length=65)
        roll =models.CharField(verbose_name="roll",max_length=65,default="dealer")
        password =models.CharField(verbose_name=" password", max_length=65 )
        location=models.CharField(verbose_name=" location", max_length=65 )

class CustomerSignup(models.Model):
    customer_id =  models.CharField(verbose_name="customer_id",max_length=65)
    first_name =  models.CharField(verbose_name="first_name",max_length=65)
    last_name = models.CharField(verbose_name="last_name",max_length=65)
    gender = models.CharField(verbose_name="gender",max_length=65)
    gender = models.CharField(verbose_name="gender",max_length=65)
    phone_number = models.CharField(verbose_name="phone_number",max_length=10)
    email =models.CharField(verbose_name="email",max_length=65)
    roll =models.CharField(verbose_name="roll",max_length=65,default="customer")
    password =models.CharField(verbose_name=" password", max_length=65 )
    location=models.CharField(verbose_name=" location", max_length=500 )


        

from django.shortcuts import render
from django.urls import reverse
from .models import Product,Batch,Inventory
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
import mysql.connector as sql

# Create your views here.
def list_product(request):
    product_list = Product.objects.all().values()
    context = {
      'product_list': product_list,
      }
    template = loader.get_template('product_view.html')
    return HttpResponse(template.render(context, request))

def addrecord(request):
    product_id = request.POST['product_id']
    product_name = request.POST['product_name']
    model_name = request.POST['model_name']
    price = request.POST['price']
    warranty = request.POST['warranty']

    Product(product_id=product_id,product_name=product_name, model_name=model_name,price=price,warranty=warranty).save()
    return HttpResponseRedirect(reverse('list_product'))


def batch(request): 

    m=sql.connect(user='root',password="Prajitharaghu1")
    cursor=m.cursor()
    c="SELECT * FROM product_management.product_batch LEFT JOIN  product_management.product_product ON product_management.product_product.product_id = product_management.product_batch.product_id_id;"
    cursor.execute(c)
    product_list=cursor.fetchall()
    product=Product.objects.all().values()

    template = loader.get_template('batch_view.html')
  
    context = {
    
    "product_list":product_list,
    "product":product
    }
    return HttpResponse(template.render(context, request))


def batchrecord(request):
    obj = Batch.objects.count()
    Batch_Qty = request.POST['batch_Qty']
    Batch_Date = request.POST['batch_Date']
    Batch_ID = 'BATCH-'+str(Batch_Date)+"/"+str(obj)
    Product_id=request.POST['product_id_id']

    Inventory_id="INV_PRODECTNAME"+str(obj)
   
    Batch(batch_ID=Batch_ID, batch_Qty=Batch_Qty,batch_Date=Batch_Date,product_id_id=Product_id).save()
    for i in range (int(Batch_Qty)):
        Inventory(batch_ID_id=Batch_ID,product_id_id=Product_id,inventory_id=Inventory_id).save()
    
    return HttpResponseRedirect(reverse('batch'))


def inventory(request):
    m=sql.connect(user='root',password="Prajitharaghu1")
    cursor=m.cursor()
    c="SELECT * FROM product_management.product_inventory LEFT JOIN  product_management.product_product ON product_management.product_product.product_id = product_management.product_inventory.product_id_id group by status ,batch_ID_id;"
    cursor.execute(c)
    inventory_list=cursor.fetchall()
    # inventory = Inventory.objects.all().values()
    # inv=Inventory.objects.all().values('status','inventory_id','batch_ID_id','product_id_id').annotate(total=Count('status'))
    template = loader.get_template('inventory.html')

    context = {
      'inventory': inventory_list,
      
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def custemer_Product(request):
    # product_list = Product.objects.all().values()
    # context = {
    #   'product_list': product_list,
    #   }
    template = loader.get_template('customer_Page.html')
    return HttpResponse(template.render({}, request))

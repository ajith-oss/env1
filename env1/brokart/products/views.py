from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator
# Create your views here
def index(request):
    return render(request,'index.html')
def list_products(request):
    """ _summary__
    return products list page
    Args:
    request(_type_):_description_
    Returns:
    _type_:_description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=product.objects.all()
    product_paginator=Paginator(product_list,8)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products_layout.html',context)
def detail_product(request,pk):
    Product=product.objects.get(pk=pk)
    context={'product':Product}
    return render(request,'product_details.html',context)

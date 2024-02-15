from django.shortcuts import render,redirect
from . models import order,orderItem
from products.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    print("user",user)
    print("customer",customer)
    cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.cart_stage
            
        )
    context={'cart':cart_obj}
    
    return render(request,'cart.html',context)
def remove_item_from_cart(request,pk):
    item=orderItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=order.objects.get(
                owner=customer,
                order_status=order.cart_stage
                
            )
            if order_obj:
                
                order_obj.order_status=order.order_confirmed
                order_obj.total_price=total
                order_obj.save()
                status_message="your order is proccessed.your item will be delivered"
                messages.success(request,status_message)
            else:
                status_message="unbale to process your order.No item in cart"
                messages.error(request,status_message)
        except Exception as e:
            status_message="unbale to process your order.No item in cart"
            messages.error(request,status_message)
       
    return redirect('cart')
@login_required(login_url='account')
def view_order(request):
    user=request.user
    customer=user.customer_profile
    all_orders=order.objects.filter(owner=customer).exclude(order_status=order.cart_stage)
    context={'orders':all_orders}
    return render(request,'orders.html',context)
            
                
@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.cart_stage
            
        )
        Product=product.objects.get(pk=product_id)
        order_item,created=orderItem.objects.get_or_create(
            product=Product,
            owner=cart_obj,
        )
        if created:
            order_item.quantity=quantity
            order_item.save()
        else:
            order_item.quantity=order_item.quantity+quantity
            order_item.save()
    return redirect('cart')
        
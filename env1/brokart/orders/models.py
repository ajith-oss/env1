from django.db import models
from customers.models import customer
from products.models import product
class order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    cart_stage=0
    order_confirmed=1
    order_processed=2
    order_delivered=3
    order_rejected=4
    status_choice=((order_processed,"order_processed"),
                   (order_delivered,"order_delivered"),
                   (order_rejected,"order_rejected"),
                   (order_confirmed,"order_confirmed"))
    order_status=models.IntegerField(choices=status_choice,default=cart_stage)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.user.username)

    
class orderItem(models.Model):
    product=models.ForeignKey(product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_item')
    
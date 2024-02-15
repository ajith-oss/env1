from django.contrib import admin
from orders.models import order,orderItem
class orderAdmin(admin.ModelAdmin):
    list_filter=[
         "owner",
         "order_status",
        
    ]
    search_fields=(
         "owner",
         "id",
    )
   

# Register your models here.
admin.site.register(order,orderAdmin)
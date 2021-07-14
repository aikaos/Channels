from django.contrib import admin
from .models import Channel, Price, Discount,\
    Day, Order, OrderDetail
# Register your models here.


admin.site.register(Channel)
admin.site.register(Price)
admin.site.register(Discount)
admin.site.register(Day)
admin.site.register(Order)
admin.site.register(OrderDetail)

from datetime import datetime

from django.db import models


# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='img/channel/logo', blank=True, null=True)
    active = models.BooleanField(default=True)
    order_num = models.IntegerField()


class Price(models.Model):
    price = models.FloatField(verbose_name='Price')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31, 12, 59))
    channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING,
                                related_name='Price')


class Discount(models.Model):
    min_days = models.IntegerField()
    percent = models.IntegerField()
    channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING,
                                related_name='Discount')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()


class Order(models.Model):
    text = models.CharField(max_length=500, verbose_name='text')
    name = models.CharField(max_length=100, verbose_name='name')
    phone = models.CharField(max_length=50, verbose_name='phone')
    email = models.CharField(max_length=100, verbose_name='email')
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    total_price = models.FloatField(verbose_name='Total price')
    STATUS_CHOICES = [(0, 'not paid'),
                      (1, 'paid'),
                      (2, 'payment expired')]

    status = models.IntegerField(choices=STATUS_CHOICES)


class OrderDetail(models.Model):
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING,
                                related_name='OrderDetail')


class Day(models.Model):
    days = models.DateField()
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.DO_NOTHING)


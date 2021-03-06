# Generated by Django 3.2.5 on 2021-07-14 04:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='img/channel/logo')),
                ('active', models.BooleanField(default=True)),
                ('order_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='text')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('total_price', models.FloatField(verbose_name='Total price')),
                ('status', models.IntegerField(choices=[(0, 'not paid'), (1, 'paid'), (2, 'payment expired')])),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Price')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2999, 12, 31, 12, 59))),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Price', to='channel_app.channel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='OrderDetail', to='channel_app.channel')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='channel_app.order')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_days', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Discount', to='channel_app.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DateField()),
                ('order_detail', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='channel_app.orderdetail')),
            ],
        ),
    ]

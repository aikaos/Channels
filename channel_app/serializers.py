from rest_framework import serializers

from .models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['min_days', 'percent']


class ChannelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    photo = serializers.ImageField()
    price = serializers.FloatField()
    discount = DiscountSerializer(many=True)






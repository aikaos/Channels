from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .dto import ChannelDto, get_channel_dto
from .models import Channel

from .serializers import  ChannelSerializer


@api_view(['GET'])
def channel_ad_list(request):
    if request.method == 'GET':
        list = Channel.objects.filter(active=True)
        channel_dto = get_channel_dto(list)
        serializer = ChannelSerializer(channel_dto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

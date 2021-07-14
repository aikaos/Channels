from django.urls import path

from . import views

urlpatterns = [
    path('channel/list/', views.channel_ad_list)

]
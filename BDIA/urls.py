from django.contrib import admin
from django.urls import path
from dabank import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login-page/', views.login),
    path('new-customer/', views.create_customer, name="new-customer"),
    path('transfer/', views.money_transfer, name='transfer')
]

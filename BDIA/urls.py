from django.contrib import admin
from django.urls import path
from dabank import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new-customer/', views.create_customer, name="new-customer"),
    path('transfer/', views.money_transfer, name='transfer')
]

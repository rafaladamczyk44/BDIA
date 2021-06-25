from django.db import models


# Stwórz tabelę dla klienta
class Customer(models.Model):
    personal_id = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    customer_num = models.CharField(max_length=8)
    account_num = models.CharField(max_length=14)
    age = models.IntegerField()


# Stwórz tabelę konta bankowego
class Account(models.Model):
    acc_num = models.CharField(unique=True, max_length=14)
    acc_balance = models.FloatField()
    acc_owner_id = models.CharField(max_length=8)

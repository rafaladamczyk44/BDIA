from django.db import models


# Stwórz tabelę dla klienta
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    cust_acc_number = models.IntegerField()

    def __str__(self):
        return self.first_name + self.last_name


# Stwórz tabelę konta bankowego
class Account(models.Model):
    acc_num = models.IntegerField(unique=True)
    acc_balance = models.FloatField()
    acc_owner_id = models.IntegerField()

    def ask_for_money(self):
        return self.acc_balance

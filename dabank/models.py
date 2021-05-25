from django.db import models
from django.db import transaction  # nadpisz domyślne zachowanie


# Stworzenie modeli dla baz danych
# będzie to pokazane jako tabele

# Stwórz tabelę dla klienta
class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
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

    def put(self, request): # TODO: Atomic transaction
        # Atomic isolation level
        with transaction.atomic():
            pass

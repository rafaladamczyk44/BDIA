from django.shortcuts import render
from django.http import HttpResponseRedirect
from dabank.models import Customer, Account
from dabank.forms import *
from dabank.numbers_generator import create_card_number
from django.db import IntegrityError
from django.db import transaction

# TODO: endpoints


def index(request):
    return render(request, 'index.html')


# Tworzenie klienta
def create_customer(request):
    if request.method == 'POST':
        form = CreateCustomer(request.POST)

        # Walidacja formy
        if form.is_valid():
            # Zapobieganie auto-commit
            # Atomowość commitu zapobiega tu utworzenia w bazie zarówno dwóch takich samych klientów jak i dwóch kont

            with transaction.atomic():
                pers_id = form.cleaned_data['personal_id']
                f_name = form.cleaned_data['first_name']
                l_name = form.cleaned_data['last_name']
                age = form.cleaned_data['age']
                account_num = account_number()
                customer_num = int(str(account_num)[:8])
                print(account_num, customer_num)

                # Utwórz klienta na podstawie modelu Customer
                customer = Customer(personal_id=pers_id,
                                    first_name=f_name,
                                    last_name=l_name,
                                    customer_num=customer_num,
                                    age=age)

                try:
                    customer.save()
                    print("Customer saved")
                    # Gdy stworzy kliena próbuje stworzyć konto
                    try:
                        account = Account(acc_num=account_num,
                                          acc_balance=0,
                                          acc_owner_id=customer_num)
                        account.save()
                        print("Account saved")
                    except IntegrityError:
                        print('Account integrity error')

                    return HttpResponseRedirect('/new-customer/')
                # Złap integrity error - kiedy element się powtarza
                except IntegrityError:
                    print("Integrity error")
                    return HttpResponseRedirect('/')
    else:
        form = CreateCustomer()

    return render(request, 'new_customer.html', {'form': form})


def login(request):
    return render(request, 'login-page.html')


def account_number():
    # Wykorzystanie odwrotnego algorytmu Luhn'a do stworzenia porpawnego numeru karty
    number = create_card_number()
    return number


def money_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['from_acc']
            num2 = form.cleaned_data['to_acc']
            amount = form.cleaned_data['amount']

            # Zablokuj commit jeśli drugie konto (to_acc) nie istnieje
            # Nie updatetuj wartości "balance"
            with transaction.atomic():
                """
                select_for_update - blockuje (lock) transakcje -
                nie może być podjęta inan operacja dopóki ta się nie zakończy
                https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.select_for_update
                Lock zdejmowany jest automatycznie
                w tym przypadku cały row jest blokowany do momentu zakończenia operacji
                nowait=True renders the call non-blocking
                """
                from_acc = Account.objects.select_for_update(nowait=True).get(acc_num=num1)
                from_acc.acc_balance = from_acc.acc_balance - amount
                from_acc.save()

                to_acc = Account.objects.select_for_update().get(acc_num=num2)
                to_acc.acc_balance = to_acc.acc_balance + amount
                to_acc.save()

            return HttpResponseRedirect('/transfer/')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form})

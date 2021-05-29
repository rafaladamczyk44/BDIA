from django.shortcuts import render
from django.http import HttpResponseRedirect
from dabank.models import Customer, Account
from dabank.forms import *
# TODO: Stworzyć funkcję dla tworzenia konta


def money_transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = TransferForm()

    return render(request, 'transfer.html', {'form': form})


def create_customer(request):
    if request.method == 'POST':
        form = CreateCustomer(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            customer = Customer(first_name=f_name, last_name=l_name, age=age, cust_acc_number=0000)
            customer.save()
            print(customer)
            return HttpResponseRedirect('new-customer/')
    else:
        form = CreateCustomer()

    return render(request, 'new_customer.html', {'form': form})

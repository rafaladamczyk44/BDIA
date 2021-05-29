from django import forms


class TransferForm(forms.Form):
    from_acc = forms.CharField(label="From account", max_length=14)
    to_acc = forms.CharField(label="To account", max_length=14)
    amount = forms.IntegerField(label="Amount", min_value=1)


class CreateCustomer(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=100)
    last_name = forms.CharField(label='Nazwisko', max_length=100)
    age = forms.IntegerField(label='Wiek', min_value=18)


class CreateAccount(forms.Form):
    customer_num = forms.CharField(label='Numer klienta', max_length=100)
from django.contrib import admin
from dabank.models import Customer, Account


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('personal_id', 'customer_num', 'first_name', 'last_name', 'age',)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('acc_num', 'acc_balance', 'acc_owner_id')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Account, AccountAdmin)

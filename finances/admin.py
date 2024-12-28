from django.contrib import admin

from .models import Expense, Revenue, Person, Investment

admin.site.register(Expense)
admin.site.register(Revenue)
admin.site.register(Person)
admin.site.register(Investment)
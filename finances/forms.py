from django import forms

from .models import Person, CardFatura, Expense, Investment, Revenue


class RegisterPersonForm(forms.ModelForm):
    class Meta:
        model= Person
        fields = '__all__'

class RegisterCardForm(forms.ModelForm):
    class Meta:
        model=CardFatura
        fields = '__all__'

class RegisterExpenseForm(forms.ModelForm):
    class Meta:
        model= Expense
        fields = '__all__'  

class RegisterRevenueForm(forms.ModelForm):
    class Meta:
        model=Revenue
        fields = '__all__' 


class RegisterInvestmentForm(forms.ModelForm):
    class Meta:
        model=Investment
        fields = '__all__' 


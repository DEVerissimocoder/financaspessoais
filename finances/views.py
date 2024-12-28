from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterPersonForm, RegisterExpenseForm, RegisterCardForm, RegisterRevenueForm, RegisterInvestmentForm
from .models import Person, CardFatura, Expense, Revenue, Investment
from django.urls import reverse_lazy


def index (request):   
    
    return render(request, 'index.html')


# PERSON
def registerPerson(request):
    if request.method=='POST':
        form = RegisterPersonForm(request.POST)
        if form.is_valid():
            print("formulário valido")
            form.save()
            return render(request, "person/registerPerson.html")
        else:
            print("formulario inválido", form.errors)
   
    return render(request, "person/registerPerson.html", {"formPerson":RegisterPersonForm})

def listPerson(request):
    person = Person.objects.getAll()
    return render(request, "person/listPerson.html", {"person": person})

# CARD
def registerCard(request):
    if request.method=='POST':
        form = RegisterCardForm(request.POST)
        if form.is_valid():
            print("formulário valido")
            form.save()
            return render(request, "card/listCard.html")
        else:
            print("formulario inválido", form.errors)
    
    return render(request, "card/registerCard.html", {"formCard":RegisterCardForm})

def listCard(request):
    card = CardFatura.objects.getAll()
    return render(request, "card/listCard.html", {"card": card})

#EXPENSE
def registerExpense(request):
    if request.method=='POST':
        form = RegisterExpenseForm(request.POST)
        if form.is_valid():
            print("formulário valido")
            form.save()
            return HttpResponseRedirect(reverse_lazy('listExpense'))
        else:
            print("formulario inválido", form.errors)
    
    return render(request, "expense/registerExpense.html", {"formExpense":RegisterExpenseForm})

def alterExpense(request, pk):
    despesa = get_object_or_404(Expense, pk = pk)
    if request.method=='POST':
        form = RegisterExpenseForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('listExpense'))
    else:
        form = RegisterExpenseForm(instance=despesa)
    return render(request, 'expense/alterExpense.html', {'formExpense': form, 'pk':pk})

def deleteExpense(request, pk):
    expense = get_object_or_404(Expense, pk = pk)
    expense.delete()
    return HttpResponseRedirect(reverse_lazy('listExpense'))

def listExpense(request):
    expense = Expense.objects.all()
    expenses = Expense.objects.values_list('value', flat=True)
    tot = sum(expenses)
    return render(request, 'expense/listExpense.html', {"expenses": expense, 'totExpense': tot})


#REVENUE
def registerRevenue(request):
    if request.method=='POST':
        form = RegisterRevenueForm(request.POST)
        if form.is_valid():
            print("formulário valido")
            form.save()
            return HttpResponseRedirect(reverse_lazy('listRevenue'))
        else:
            print("formulario inválido", form.errors)
    
    return render(request, "revenue/registerRevenue.html", {"formRevenue":RegisterRevenueForm})

def listRevenue(request):
    revenue = Revenue.objects.all()
    revenues = Revenue.objects.values_list('value', flat=True)
    tot=sum(revenues)
    print(tot)
    return render(request, 'revenue/listRevenue.html', {'revenues': revenue, 'totRevenue': tot})

def alterRevenue(request, pk):
    revenue = get_object_or_404(Revenue, pk=pk)
    if request.method=='POST':
        form = RegisterRevenueForm(request.POST, instance=revenue)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('listRevenue'))
    else:
        form = RegisterRevenueForm(instance=revenue)
    return render(request, 'revenue/alterRevenue.html', {'formRevenue': form, 'pk':pk})
    
def deleteRevenue(request, pk):
    revenue = get_object_or_404(Revenue, pk = pk)
    revenue.delete()
    return HttpResponseRedirect(reverse_lazy('listRevenue'))

#INVESTMENT
def registerInvestment(request):
    if request.method=='POST':
        form = RegisterInvestmentForm(request.POST)
        if form.is_valid():
            print("formulário valido")
            form.save()
            return render(request, "investment/listInvestment.html")
        else:
            print("formulario inválido", form.errors)
    
    return render(request, "investment/registerInvestment.html", {"formInvestment":RegisterInvestmentForm})

def listInvestiment(request):

    investment = Investment.objects.all()
    return render(request, 'investment/listInvestment.html', {'investment': investment})


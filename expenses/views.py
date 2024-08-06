from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense
from .forms import ExpenseForm
import json

def expense_list(request):
    expenses = Expense.objects.all()
    total_amount = sum(expense.amount for expense in expenses)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_amount': total_amount})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def subtract_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.amount = -expense.amount  # Subtract the amount
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/subtract_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    return redirect('expense_list')

def backup_expenses(request):
    expenses = Expense.objects.all()
    data = [{'name': expense.name, 'amount': str(expense.amount), 'date': str(expense.date)} for expense in expenses]
    return JsonResponse(data, safe=False)

def restore_expenses(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for expense in data:
            Expense.objects.create(name=expense['name'], amount=expense['amount'], date=expense['date'])
        return JsonResponse({'message': 'Expenses restored successfully'})
    return JsonResponse({'message': 'Invalid request'})

def render_expenses(request):
    expenses = Expense.objects.all()
    total_amount = sum(expense.amount for expense in expenses)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_amount': total_amount})

def add_amount(request, amount):
    expense = Expense.objects.create(amount=amount)
    return redirect('expense_list')

def subtract_amount(request, amount):
    expense = Expense.objects.create(amount=-amount)
    return redirect('expense_list')

def animate_total_amount(request):
    total_amount = sum(expense.amount for expense in Expense.objects.all())
    return JsonResponse({'total_amount': total_amount})

def render_calendar(request, year):
    expenses = Expense.objects.filter(date__year=year)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    data = []
    for month in months:
        total_amount = sum(expense.amount for expense in expenses.filter(date__month=months.index(month) + 1))
        data.append({'month': month, 'total_amount': total_amount})
    return JsonResponse(data, safe=False)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('sub/', views.subtract_expense, name='subtract_expense'),
    path('delete/<pk>/', views.delete_expense, name='delete_expense'),
    path('backup/', views.backup_expenses, name='backup_expenses'),
    path('restore/', views.restore_expenses, name='restore_expenses'),
    path('render/', views.render_expenses, name='render_expenses'),
    path('add_amount/<amount>/', views.add_amount, name='add_amount'),
    path('subtract_amount/<amount>/', views.subtract_amount, name='subtract_amount'),
    path('animate_total_amount/', views.animate_total_amount, name='animate_total_amount'),
    path('render_calendar/<year>/', views.render_calendar, name='render_calendar'),
]
from django.urls import path
from .views import ExpenseListCreateView, ExpenseTetrivelUpdateDestroyView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name = 'expense-list-create'),
    path('expenses/<int:pk>/', ExpenseTetrivelUpdateDestroyView.as_view(), name  = 'expense-retrieve-update-destroy'),
]

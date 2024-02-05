from django.shortcuts import render
from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializers

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializers

class ExpenseTetrivelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializers

    
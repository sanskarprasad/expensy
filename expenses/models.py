from django.db import models

class Expense(models.Model):
    amount = models.FloatField()
    category = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    date = models.DateField(auto_now = True)

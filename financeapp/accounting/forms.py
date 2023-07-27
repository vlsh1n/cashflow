from django import forms
from .models import Transaction, Category, Pool, StorageLocation


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'description', 'type']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['name', 'distribution_percentage']


# class StorageLocationForm(forms.ModelForm):
#     class Meta:
#         model = StorageLocation
#         fields = ['name', 'description']

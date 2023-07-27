from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View

from .forms import TransactionForm, CategoryForm, PoolForm #StorageLocationForm
from .models import Transaction, Category, Pool #StorageLocation


# Main view for home page
def home_view(request):
    return render(request, 'home.html')


# View for registration page
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})


# List of views for CATEGORIES CRUD
@login_required
def categories_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'view_categories.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category added!')
            return redirect('categories-list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('categories-list')
    return render(request, 'category_delete.html', {'category': category})


# List of views for TRANSACTIONS CRUD
@login_required
def transactions_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'view_transactions.html', {'transactions': transactions})


@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction added!')
            return redirect('transactions-list')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})


@login_required
def transaction_edit(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions-list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction_edit.html', {'form': form})


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions-list')
    return render(request, 'transaction_delete.html', {'transaction': transaction})


# List of views for POOLS CRUD
@login_required
def pools_list(request):
    pools = Pool.objects.filter(user=request.user)
    return render(request, 'view_pools.html', {'pools': pools})


@login_required
def pool_create(request):
    if request.method == "POST":
        form = PoolForm(request.POST)
        if form.is_valid():
            pool = form.save(commit=False)
            pool.user = request.user
            pool.save()
            return redirect('pools-list')
    else:
        form = PoolForm()
    return render(request, 'add_pool.html', {'form': form})


@login_required
def pool_edit(request, pk):
    pool = get_object_or_404(Pool, pk=pk)
    if request.method == "POST":
        form = PoolForm(request.POST, instance=pool)
        if form.is_valid():
            pool = form.save()
            return redirect('pools-list')
    else:
        form = PoolForm(instance=pool)
    return render(request, 'pool_edit.html', {'form': form})


@login_required
def pool_delete(request, pk):
    pool = get_object_or_404(Pool, pk=pk)
    if request.method == "POST":
        pool.delete()
        return redirect('pools-list')
    return render(request, 'pool_delete.html', {'pool': pool})


# List of views for STORAGE CRUD
# @login_required
# def storage_locations_list(request):
#     storage_locations = StorageLocation.objects.filter(user=request.user)
#     return render(request, 'view_storage_locations.html', {'storage_locations': storage_locations})
#
#
# @login_required
# def storage_location_create(request):
#     if request.method == "POST":
#         form = StorageLocationForm(request.POST)
#         if form.is_valid():
#             storage_location = form.save(commit=False)
#             storage_location.user = request.user
#             storage_location.save()
#             return redirect('storages-list')
#     else:
#         form = StorageLocationForm()
#     return render(request, 'add_storage.html', {'form': form})
#
#
# @login_required
# def storage_location_edit(request, pk):
#     storage_location = get_object_or_404(StorageLocation, pk=pk)
#     if request.method == "POST":
#         form = StorageLocationForm(request.POST, instance=storage_location)
#         if form.is_valid():
#             storage_location = form.save()
#             return redirect('storages-list')
#     else:
#         form = StorageLocationForm(instance=storage_location)
#     return render(request, 'storage_edit.html', {'form': form})
#
#
# @login_required
# def storage_location_delete(request, pk):
#     storage_location = get_object_or_404(StorageLocation, pk=pk)
#     if request.method == "POST":
#         storage_location.delete()
#         return redirect('storages-list')
#     return render(request, 'storage_delete.html', {'storage_location': storage_location})

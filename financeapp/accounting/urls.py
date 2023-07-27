from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home_view, name='home'),

    # Registration URLs
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Transaction URLs
    path('transactions-list/', views.transactions_list, name='transactions-list'),
    path('transaction/create/', views.transaction_create, name='transaction_create'),
    path('transaction/<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('transaction/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    # Category URLs
    path('categories-list/', views.categories_list, name='categories-list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Pool URLs
    path('pools-list/', views.pools_list, name='pools-list'),
    path('pool/create/', views.pool_create, name='pool_create'),
    path('pool/<int:pk>/edit/', views.pool_edit, name='pool_edit'),
    path('pool/<int:pk>/delete/', views.pool_delete, name='pool_delete'),

    # # Storage Location URLs
    # path('storages-list/', views.storage_locations_list, name='storages-list'),
    # path('storage/create/', views.storage_location_create, name='storage_create'),
    # path('storage/<int:pk>/edit/', views.storage_location_edit, name='storage_edit'),
    # path('storage/<int:pk>/delete/', views.storage_location_delete, name='storage_delete'),
]

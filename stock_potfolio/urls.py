# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stocks/', views.stock_list, name='stock_list'),
    path('stocks/<int:stock_id>/', views.stock_detail, name='stock_detail'),
    path('stocks/create/', views.stock_create, name='stock_create'),
    path('stocks/<int:stock_id>/update/', views.stock_update, name='stock_update'),
    path('stocks/<int:stock_id>/delete/', views.stock_delete, name='stock_delete'),
]

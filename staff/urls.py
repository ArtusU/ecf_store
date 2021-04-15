from django.urls import path
from . import views


app_name = 'staff'

urlpatterns = [
    path('', views.StaffViews.as_view(), name='staff'),
    path('create', views.ProductCreateView.as_view(), name='product-create'),
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('product/<pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
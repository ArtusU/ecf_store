
from django.urls import path, include
from . import views

app_name = 'distribution'

urlpatterns = [
    path('', views.DistributionListView.as_view(), name='distribution-list'),
    path('change-delivery-day/<pk>/', views.ChangeDeliveryDay.as_view(), name='change-delivery-day'),
    path('change-delivery-run/<pk>/', views.ChangeDeliveryRun.as_view(), name='change-delivery-run'),
    path('change-delivery-stage/<pk>/', views.ChangeDeliveryStage.as_view(), name='change-delivery-stage'),
]
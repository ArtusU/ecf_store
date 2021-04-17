
from django.urls import path, include
from . import views

app_name = 'distribution'

urlpatterns = [
    path('', views.DistributionListView.as_view(), name='distribution-list')
]
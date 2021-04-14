from django.urls import path
from . import views


app_name = 'staff'

urlpatterns = [
    path('', views.StaffViews.as_view(), name='staff')
]
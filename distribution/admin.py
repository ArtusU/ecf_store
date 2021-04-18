from django.contrib import admin
from .models import OrderDistribution



class OrderDistributionAdmin(admin.ModelAdmin):
    list_display = ['order',
                    'delivery_day',
                    'delivery_run',
                    'order_stage']

admin.site.register(OrderDistribution, OrderDistributionAdmin)

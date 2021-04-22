import django_filters
from distribution.models import OrderDistribution




class OrderDistributionFilter(django_filters.FilterSet):
    #order__user__email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = OrderDistribution
        fields = ['delivery_day', 'delivery_run', 'order_stage', 'archive']
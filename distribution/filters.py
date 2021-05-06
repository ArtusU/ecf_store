import django_filters
from distribution.models import OrderDistribution




class OrderDistributionFilter(django_filters.FilterSet):
    order__user__email = django_filters.CharFilter(lookup_expr='icontains')
    order__shipping_address__post_code = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = OrderDistribution
        fields = [ 'order__user__email', 'delivery_day', 'delivery_run', 'order_stage', 'order__shipping_address__post_code', 'archive']
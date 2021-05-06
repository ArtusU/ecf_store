import django_filters
from cart.models import Order
from django_filters import DateFilter


class StaffCustomerFilter(django_filters.FilterSet):
    user__email = django_filters.CharFilter(lookup_expr='icontains')
    shipping_address__post_code = django_filters.CharFilter(lookup_expr='icontains')
    #user__username = django_filters.CharFilter(lookup_expr='icontains')
    # start_date = DateFilter(field_name='ordered_date', lookup_expr='gte')
    # end_date = DateFilter(field_name='ordered_date', lookup_expr='lt')

    class Meta:
        model = Order
        fields = ['user__email', 'shipping_address__post_code']

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from cart import models
from distribution.models import OrderDistribution

class DistributionListView(LoginRequiredMixin, generic.ListView):
    template_name = 'distribution/distribution.html'

    #queryset = OrderDistribution.objects.filter(order__ordered = True).order_by('-order__ordered_date')
    queryset = OrderDistribution.objects.all()
    context_object_name = 'orders'



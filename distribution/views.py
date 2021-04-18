from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, reverse

from django.views import generic

from cart import models
from distribution.models import OrderDistribution

class DistributionListView(LoginRequiredMixin, generic.ListView):
    template_name = 'distribution/distribution.html'
    queryset = OrderDistribution.objects.filter(order__ordered=True).order_by('-order__ordered_date')
    context_object_name = 'orders'

    


class ChangeDeliveryDay(generic.View): 
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderDistribution, id=kwargs['pk'])
        order_item.delivery_day = self.request.GET.get('delivery_day', None)
        order_item.save()
        return redirect("distribution:distribution-list")


class ChangeDeliveryRun(generic.View): 
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderDistribution, id=kwargs['pk'])
        order_item.delivery_run = self.request.GET.get('delivery_run', None)
        order_item.save()
        return redirect("distribution:distribution-list")


class ChangeDeliveryStage(generic.View): 
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderDistribution, id=kwargs['pk'])
        order_item.order_stage = self.request.GET.get('order_stage', None)
        order_item.save()
        return redirect("distribution:distribution-list")



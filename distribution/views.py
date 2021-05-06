from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render

from django.views import generic

from cart import models
from distribution.models import OrderDistribution
from cart.models import Order, Payment
from distribution.filters import OrderDistributionFilter

class DistributionListView(LoginRequiredMixin, generic.ListView):
    template_name = 'distribution/distribution.html'
    context_object_name = 'orders'

    def get_queryset(self):
        qs = OrderDistribution.objects.filter(order__ordered=True).order_by('-order__ordered_date')
        return qs

    def get_context_data(self, **kwargs):
        context = super(DistributionListView, self).get_context_data(**kwargs)
        context.update({
            "myFilter": OrderDistributionFilter(self.request.GET, queryset=self.get_queryset())
        })
        return context

    

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


class DistributionDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'distribution/distribution_detail.html'
    #queryset = Order.objects.all()
    queryset = OrderDistribution.objects.filter(order__ordered=True)
    context_object_name = 'order'


# class DailyDistributionListView(generic.ListView):
#     template_name = 'distribution/daily_distribution.html'
#     context_object_name = 'orders'

#     def get_queryset(self):
#         qs = OrderDistribution.objects.filter(order__ordered=True)
#         delivery_day = self.request.GET.get('delivery_day', None)
#         if delivery_day:
#             qs = qs.filter(delivery_day=delivery_day)
#         return qs


# class DailyRunDistributionListView(generic.ListView):
#     template_name = 'distribution/daily_run_distribution.html'
#     context_object_name = 'orders'

#     # def get_deliveryday(self, **kwargs):
#     #     return self.request.GET.get('delivery_day', None)
#     #     print(get_deliveryday())

#         #return get_object_or_404(OrderDistribution, delivery_day=self.kwargs["delivery_day"])

#     def dispatch(self, request, *args, **kwargs):
#         kwargs["delivery_day"] = self.request.GET.get('delivery_day', None)
#         return super().dispatch(request, *args, **kwargs)
        
        
    

#     def get_queryset(self):
#         qs = OrderDistribution.objects.filter(order__ordered=True)
#         delivery_day = self.request.GET.get(self.kwargs["delivery_day"])
#         delivery_run = self.request.GET.get('delivery_run', None)
#         print(self.get_deliveryday())
#         print(delivery_run)
#         if delivery_run:
#             qs = qs.filter(delivery_day=delivery_day, delivery_run=delivery_run)
#         return qs
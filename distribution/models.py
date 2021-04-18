from django.db import models
from django.db.models.signals import post_save


from cart.models import Order



DAY = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)

RUN = (
    ('1', '1'),
    ('3', '2'),
    ('4', '3'),
    ('2', '4'),
    ('5', '5'),
)

STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('OFD', 'OFD'),
        ('Delivered', 'Delivered'),
        ('SO', 'SO'),
    )
class OrderDistribution(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    delivery_day = models.CharField(max_length=50, choices=DAY, blank=True)
    delivery_run = models.CharField(max_length=50, choices=RUN, blank=True)
    order_stage = models.CharField(max_length=50, choices=STATUS, blank=True)

    archive = models.BooleanField(default=False)


    def __str__(self):
        return self.order.reference_number


def post_save_order_receiver(sender, instance, created, *args, **kwargs):
    if created:
        OrderDistribution.objects.create(order=instance)

post_save.connect(post_save_order_receiver, sender=Order)




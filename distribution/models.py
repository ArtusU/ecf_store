from django.db import models


from cart.models import Order



DAY = (
    ('Mo', 'Monday'),
    ('Tu', 'Tuesday'),
    ('We', 'Wednesday'),
    ('Th', 'Thursday'),
    ('Fr', 'Friday'),
)

RUN = (
    ('1', 'Run 1'),
    ('3', 'Run 2'),
    ('4', 'Run 3'),
    ('2', 'Run 4'),
    ('5', 'Run 5'),
)

STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('SO', 'Standing Order'),
    )
class OrderDistribution(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    delivery_day = models.CharField(max_length=20, choices=DAY)
    delivery_run = models.CharField(max_length=20, choices=RUN)
    order_stage = models.CharField(max_length=20, choices=STATUS)

    archive = models.BooleanField(default=False)


    def __str__(self):
        return self.order.reference_number

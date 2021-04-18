from django.db import models


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
    delivery_day = models.CharField(max_length=50, choices=DAY)
    delivery_run = models.CharField(max_length=50, choices=RUN)
    order_stage = models.CharField(max_length=50, choices=STATUS)

    archive = models.BooleanField(default=False)


    def __str__(self):
        return self.order.reference_number

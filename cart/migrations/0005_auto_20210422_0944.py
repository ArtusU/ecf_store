# Generated by Django 3.1.7 on 2021-04-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_stripepayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripepayment',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]

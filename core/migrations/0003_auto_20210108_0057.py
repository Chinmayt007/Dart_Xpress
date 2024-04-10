# Generated by Django 3.1.3 on 2021-01-08 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_card_last4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_payment_method_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_plan_purchase_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='plan_recharge_date',
            field=models.DateField(null=True),
        ),
    ]

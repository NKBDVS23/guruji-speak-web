# Generated by Django 4.2.4 on 2023-09-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_wallet_plan_recharge_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='purchase_date',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_gurujiusers_birth_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_setting_plan_dollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name_1', models.CharField(blank=True, max_length=240, null=True)),
                ('admin_plan_1_d', models.CharField(blank=True, max_length=500, null=True)),
                ('amount_plan', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]

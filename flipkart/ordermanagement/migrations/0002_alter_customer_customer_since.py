# Generated by Django 4.2.16 on 2024-10-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_since',
            field=models.DateField(auto_now_add=True),
        ),
    ]
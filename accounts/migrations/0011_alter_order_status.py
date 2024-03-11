# Generated by Django 4.1.3 on 2024-02-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'NOT PACKED'), ('PACKED', 'PACKED'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered')], default='1', max_length=20),
        ),
    ]

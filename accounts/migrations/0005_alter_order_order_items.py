# Generated by Django 4.1.3 on 2024-02-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_cartitems_cart_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.cart'),
        ),
    ]

# Generated by Django 4.1.3 on 2024-03-06 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_updated_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='description',
        ),
    ]

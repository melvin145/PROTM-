# Generated by Django 4.1.3 on 2023-12-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_slug_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]

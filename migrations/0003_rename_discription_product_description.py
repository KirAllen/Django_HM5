# Generated by Django 4.2.5 on 2023-10-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0002_product_date_added_product_discription_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
    ]

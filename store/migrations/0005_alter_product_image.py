# Generated by Django 4.1.7 on 2023-03-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/products'),
        ),
    ]

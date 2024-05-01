# Generated by Django 5.0.4 on 2024-05-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_presentation"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity_reviews",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
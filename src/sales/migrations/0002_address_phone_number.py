# Generated by Django 5.0.4 on 2024-05-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="phone_number",
            field=models.CharField(default=666666666, max_length=255),
            preserve_default=False,
        ),
    ]
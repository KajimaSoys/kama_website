# Generated by Django 4.2.4 on 2023-09-29 21:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("delivery_page", "0002_remove_paymentblock_image_second_paymentblock_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paymentblock",
            options={
                "verbose_name": "2 - Порядок оплаты",
                "verbose_name_plural": "2 - Порядок оплаты",
            },
        ),
    ]

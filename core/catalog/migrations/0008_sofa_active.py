# Generated by Django 4.2.4 on 2023-09-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0007_alter_sofa_armrest_height_alter_sofa_back_height_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sofa",
            name="active",
            field=models.BooleanField(
                default=True, verbose_name="Опубликовано на сайте?"
            ),
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-09 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_sofaimage_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sofaimage',
            options={'ordering': ['order'], 'verbose_name': 'изображение дивана', 'verbose_name_plural': 'Изображения диванов'},
        ),
    ]
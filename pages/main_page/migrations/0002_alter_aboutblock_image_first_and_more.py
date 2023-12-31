# Generated by Django 4.2.4 on 2023-09-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutblock',
            name='image_first',
            field=models.FileField(max_length=500, upload_to='main_page/about/', verbose_name='Фото №1'),
        ),
        migrations.AlterField(
            model_name='aboutblock',
            name='image_second',
            field=models.FileField(max_length=500, upload_to='main_page/about/', verbose_name='Фото №2'),
        ),
        migrations.AlterField(
            model_name='aboutblock',
            name='image_third',
            field=models.FileField(max_length=500, upload_to='main_page/about/', verbose_name='Фото №3'),
        ),
        migrations.AlterField(
            model_name='contactsblock',
            name='image_first',
            field=models.FileField(max_length=500, upload_to='main_page/contacts/', verbose_name='Фото №1'),
        ),
        migrations.AlterField(
            model_name='contactsblock',
            name='image_second',
            field=models.FileField(max_length=500, upload_to='main_page/contacts/', verbose_name='Фото №2'),
        ),
        migrations.AlterField(
            model_name='headerblock',
            name='logo',
            field=models.FileField(max_length=500, upload_to='main_page/header/', verbose_name='Лого'),
        ),
        migrations.AlterField(
            model_name='mainblock',
            name='image',
            field=models.FileField(max_length=500, upload_to='main_page/main/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='requestblock',
            name='image',
            field=models.FileField(max_length=500, upload_to='main_page/request/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='stagesblock',
            name='image_first',
            field=models.FileField(max_length=500, upload_to='main_page/stages/', verbose_name='Фото №1'),
        ),
        migrations.AlterField(
            model_name='stagesblock',
            name='image_second',
            field=models.FileField(max_length=500, upload_to='main_page/stages/', verbose_name='Фото №2'),
        ),
    ]

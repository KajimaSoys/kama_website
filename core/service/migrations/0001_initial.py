# Generated by Django 4.2.4 on 2023-09-08 03:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Вопрос')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=500, verbose_name='Имя автора')),
                ('review', ckeditor.fields.RichTextField(verbose_name='Отзыв')),
                ('author_photo', models.FileField(blank=True, max_length=500, upload_to='core/reviews/', verbose_name='Фото автора')),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ReviewPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(max_length=500, upload_to='core/reviews/', verbose_name='Фото')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='service.review')),
            ],
            options={
                'verbose_name': 'Фото отзыва',
                'verbose_name_plural': 'Фото отзывов',
            },
        ),
    ]

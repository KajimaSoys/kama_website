# Generated by Django 4.2.4 on 2023-09-09 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_sofaimage_options'),
        ('service', '0003_alter_question_options_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewphoto',
            options={'ordering': ['order'], 'verbose_name': 'Фото отзыва', 'verbose_name_plural': 'Фото отзывов'},
        ),
        migrations.AddField(
            model_name='review',
            name='sofa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.sofa', verbose_name='Диван'),
        ),
    ]

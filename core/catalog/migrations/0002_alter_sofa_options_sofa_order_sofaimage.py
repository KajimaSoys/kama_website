# Generated by Django 4.2.4 on 2023-09-09 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sofa',
            options={'ordering': ['order'], 'verbose_name': 'диван', 'verbose_name_plural': 'Диваны'},
        ),
        migrations.AddField(
            model_name='sofa',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Порядок'),
        ),
        migrations.CreateModel(
            name='SofaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='core/catalog/sofas/', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Порядок')),
                ('sofa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.sofa', verbose_name='Диван')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]

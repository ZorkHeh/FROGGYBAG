# Generated by Django 4.0.6 on 2022-08-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('quantity', models.IntegerField(verbose_name='Колличество')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(verbose_name='Дата редактирования')),
            ],
        ),
    ]

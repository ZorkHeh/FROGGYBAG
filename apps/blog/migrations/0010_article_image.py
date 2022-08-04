# Generated by Django 4.0.6 on 2022-08-04 11:35

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='blog/article/', verbose_name='Изображение'),
        ),
    ]

# Generated by Django 2.2.8 on 2020-02-12 16:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200212_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default='azertyu', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
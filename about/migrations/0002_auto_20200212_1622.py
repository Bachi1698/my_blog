# Generated by Django 2.2.8 on 2020-02-12 16:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='presentation',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]

# Generated by Django 2.2.8 on 2020-02-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='avatar',
            field=models.ImageField(default='static/img/bg-img/48.jpg', upload_to='images/user'),
        ),
    ]

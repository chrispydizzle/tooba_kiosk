# Generated by Django 2.1 on 2018-08-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0005_auto_20180819_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='img_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]

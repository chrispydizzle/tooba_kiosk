# Generated by Django 2.1 on 2018-08-19 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0003_auto_20180819_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 7, 53, 27, 140125, tzinfo=utc), verbose_name='publish time'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 7, 53, 27, 139751, tzinfo=utc), verbose_name='publish time'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 7, 53, 27, 134404, tzinfo=utc), verbose_name='publish time'),
        ),
    ]
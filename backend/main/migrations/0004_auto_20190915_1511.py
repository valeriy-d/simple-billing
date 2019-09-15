# Generated by Django 2.2.5 on 2019-09-15 15:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190915_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencyquotesmodel',
            name='date',
        ),
        migrations.AddField(
            model_name='currencyquotesmodel',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 15, 11, 1, 999758, tzinfo=utc), verbose_name='Datetime of value'),
            preserve_default=False,
        ),
    ]
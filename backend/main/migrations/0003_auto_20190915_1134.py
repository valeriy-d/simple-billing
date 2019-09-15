# Generated by Django 2.2.5 on 2019-09-15 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_currencyquotesmodel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionmodel',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='transactionmodel',
            name='exchange_quote',
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='currency_rate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.CurrencyQuotesModel'),
            preserve_default=False,
        ),
    ]

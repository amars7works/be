# Generated by Django 2.1 on 2019-01-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_remove_remainingaccruedleaves_till_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='remainingaccruedleaves',
            name='till_date',
            field=models.DateField(null=True),
        ),
    ]

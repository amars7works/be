# Generated by Django 2.1 on 2019-06-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='activity_level',
            field=models.CharField(default='0', max_length=4),
        ),
    ]

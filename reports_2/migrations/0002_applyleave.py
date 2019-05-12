# Generated by Django 2.1 on 2019-05-07 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports_2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('leave_start_date', models.DateTimeField()),
                ('leave_end_date', models.DateTimeField()),
                ('apply_reason', models.TextField(blank=True, null=True)),
                ('leave_status', models.BooleanField(default=False)),
                ('denied_reason', models.TextField(blank=True, null=True)),
                ('Type_of_Request', models.CharField(choices=[('Sick_Leave', 'Sick Leave Request'), ('Vocational_Leave', 'Vocational Leave Request'), ('General_Leave', 'General Leave Request'), ('Night_Shift', 'Night Shift Request'), ('Work_From_Home', 'WorkFromHome Request')], max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

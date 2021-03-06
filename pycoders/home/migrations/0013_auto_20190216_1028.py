# Generated by Django 2.1.7 on 2019-02-16 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190216_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar1',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/avatar'),
        ),
        migrations.AddField(
            model_name='customer',
            name='avatar2',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/avatar'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 16, 10, 28, 32, 323491)),
        ),
    ]

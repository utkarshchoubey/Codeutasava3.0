# Generated by Django 2.1.7 on 2019-02-16 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190216_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 16, 10, 29, 0, 115806)),
        ),
    ]

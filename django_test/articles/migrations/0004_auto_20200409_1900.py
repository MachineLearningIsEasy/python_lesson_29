# Generated by Django 3.0.3 on 2020-04-09 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200408_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 19, 0, 52, 551944)),
        ),
    ]

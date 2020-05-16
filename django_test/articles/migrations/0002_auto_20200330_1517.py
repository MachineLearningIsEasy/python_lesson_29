# Generated by Django 3.0.3 on 2020-03-30 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 15, 17, 23, 89606)),
        ),
    ]

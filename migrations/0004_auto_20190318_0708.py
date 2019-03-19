# Generated by Django 2.1.7 on 2019-03-18 07:08

import datetime
from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20190313_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='date_time_delete',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 7, 8, 45, 952665)),
        ),
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(upload_to=files.models.user_path_file),
        ),
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='identifier',
            field=models.CharField(max_length=100),
        ),
    ]
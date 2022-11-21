# Generated by Django 4.1.3 on 2022-11-21 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twittertestapi', '0011_user_followingcount_alter_user_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followerCount',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='Date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2022, 11, 21, 20, 47, 34, 787060)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_service',
            name='service',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='speed_packet',
            name='ds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='speed_packet',
            name='us',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-18 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpise_data',
            name='cat',
            field=models.CharField(choices=[('Arts & Entertainment', 'ARTS'), ('Colleges & Universities', 'COLLEGE'), ('Events', 'EVENTS'), ('Food', 'FOOD'), ('Nightlife Spots', 'NIGHTLIFE'), ('Outdoors & Recreation', 'OUTDOORS'), ('Professional & Other Places', 'PROFESSIONAL'), ('Residences', 'RESIDENCES'), ('Shops & Services', 'SHOPS'), ('Travel & Transport', 'TRAVEL')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='enterpise_data',
            name='table',
            field=models.CharField(choices=[('basic', 'BASIC'), ('premium', 'PREMIUM'), ('rich', 'RICH')], default='BASIC', max_length=40),
        ),
    ]

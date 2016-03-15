# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 22:44
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediateScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intermediate_mode_score', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='MasterScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_mode_score', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='RookieScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rookie_mode_score', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=2)),
            ],
        ),
    ]

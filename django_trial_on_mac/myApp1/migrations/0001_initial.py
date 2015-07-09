# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('questionnaire', models.CharField(default='OT', max_length=2, choices=[('AP', 'Apple'), ('HP', 'Hewlett Packard'), ('DE', 'Dell'), ('TB', 'Toshiba'), ('SG', 'Samsumg'), ('AC', 'Acer'), ('AS', 'Asus'), ('SONY', 'Sony'), ('LG', 'LG'), ('OT', 'Other')])),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='entity',
            field=models.ForeignKey(to='myApp1.Entity'),
        ),
    ]

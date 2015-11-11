# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='stub',
            field=models.CharField(max_length=500, default='stub'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

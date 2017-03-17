# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address_detail',
            name='gender',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address_detail',
            name='email',
            field=models.EmailField(max_length=20, serialize=False, primary_key=True),
        ),
    ]

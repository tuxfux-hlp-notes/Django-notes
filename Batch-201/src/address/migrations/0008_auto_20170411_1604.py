# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0007_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=30)),
                ('email', models.ForeignKey(to='address.Address_Detail')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='email',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]

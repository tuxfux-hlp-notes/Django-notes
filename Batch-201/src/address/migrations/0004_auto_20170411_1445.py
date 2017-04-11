# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place', models.OneToOneField(primary_key=True, serialize=False, to='address.Place')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='waiter',
            name='restaurant',
            field=models.ForeignKey(to='address.Restaurant'),
        ),
    ]

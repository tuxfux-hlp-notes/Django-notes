# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_auto_20170411_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('pub_date',)},
        ),
        migrations.AddField(
            model_name='articles',
            name='publications',
            field=models.ManyToManyField(to='address.Publication'),
        ),
    ]

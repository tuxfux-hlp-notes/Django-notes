# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
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
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='blog.Publication'),
        ),
    ]

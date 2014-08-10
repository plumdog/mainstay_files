# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mainstay.models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, to='mainstay_files.Directory', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, mainstay.models.UpdatedAndCreated),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('directory', mptt.fields.TreeForeignKey(null=True, to='mainstay_files.Directory', blank=True)),
            ],
            options={
            },
            bases=(mainstay.models.UpdatedAndCreated, models.Model),
        ),
    ]

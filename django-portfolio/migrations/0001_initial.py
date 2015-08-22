# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'portfolio/pictures')),
                ('artwork', models.ForeignKey(related_name='pictures', to='django-portfolio.Artwork')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'picture',
                'verbose_name_plural': 'pictures',
            },
        ),
        migrations.AddField(
            model_name='artwork',
            name='categories',
            field=models.ManyToManyField(related_name='artworks', null=True, to='django-portfolio.Category', blank=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='collection',
            field=models.ForeignKey(related_name='artworks', to='django-portfolio.Collection'),
        ),
    ]

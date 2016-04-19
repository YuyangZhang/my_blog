# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_pplay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('pplay', models.CharField(max_length=1)),
                ('articles', models.CharField(max_length=2000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

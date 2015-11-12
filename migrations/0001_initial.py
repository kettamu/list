# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('check', models.BooleanField(default=False)),
                ('username', models.CharField(default='AnonymousUser', max_length=50, null=True)),
            ],
        ),
    ]

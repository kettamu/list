# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='username',
            field=models.CharField(default='guest', max_length=50, null=True),
        ),
    ]

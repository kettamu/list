from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    id = models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)
    desc = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True, auto_now_add=False)
    check = models.BooleanField(default=False)
    username = models.CharField(max_length=50, null=True, default='AnonymousUser')


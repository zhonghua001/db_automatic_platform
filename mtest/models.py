# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class A(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# Create your models here.

class B(models.Model):
    email = models.EmailField()
    address = models.CharField(max_length=50)
    userid = models.ManyToManyField(A)

class D_B(models.Model):
    charidx = models.IntegerField()

    userid = models.ManyToManyField(B)

class C(models.Model):
    capidx = models.OneToOneField(A)



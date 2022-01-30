from distutils.util import change_root
from django.db import models

# Create your models here.


class SmeEquity(models.Model):
  SYMBOL = models.CharField(max_length=150)
  NAME_OF_COMPANY = models.CharField(max_length=150)
  SERIES = models.CharField(max_length=10)
  DATE_OF_LISTING = models.DateField(auto_now=False, auto_now_add=False)
  PAID_UP_VALUE = models.IntegerField()
  ISIN_NUMBER = models.CharField(max_length=150)
  FACE_VALUE = models.IntegerField()


class Share(models.Model):
  SYMBOL = models.CharField(max_length=150)
  SERIES = models.CharField(max_length=10)
  OPEN = models.FloatField()
  HIGH = models.FloatField()
  LOW = models.FloatField()
  CLOSE = models.FloatField()
  LAST = models.FloatField()
  PREVCLOSE = models.FloatField()
  TOTTRDQTY = models.FloatField()
  TOTTRDVAL = models.FloatField()
  TIMESTAMP = models.DateField(auto_now=False, auto_now_add=False)
  TOTALTRADES = models.IntegerField()
  ISIN = models.CharField(max_length=15)


class Common(models.Model):
  SYMBOL = models.CharField(max_length=150)
  OPEN = models.FloatField()
  HIGH = models.FloatField()
  LOW = models.FloatField()
  CLOSE = models.FloatField()
  LAST = models.FloatField()
  PREVCLOSE = models.FloatField()
  TOTTRDQTY = models.FloatField()
  TOTTRDVAL = models.FloatField()
  TIMESTAMP = models.DateField(auto_now=False, auto_now_add=False)
  TOTALTRADES = models.IntegerField()
  ISIN = models.CharField(max_length=15)
  NAME_OF_COMPANY = models.CharField(max_length=150)
  DATE_OF_LISTING = models.DateField(auto_now=False, auto_now_add=False)
  PAID_UP_VALUE = models.IntegerField()
  ISIN_NUMBER = models.CharField(max_length=150)
  FACE_VALUE = models.IntegerField()

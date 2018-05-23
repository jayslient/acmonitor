# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models


class Apinform(models.Model):
    ap_oid = models.CharField(primary_key=True, max_length=60)
    ap_name = models.CharField(max_length=40, blank=True, null=True)
    ap_location = models.CharField(max_length=40, blank=True, null=True)
    ap_warning = models.CharField(max_length=3, blank=True, null=True)
    ap_remarks = models.CharField(max_length=50, blank=True, null=True)
    ap_warnsw = models.CharField(max_length=3, blank=True, null=True)
    ap_status = models.CharField(max_length=3, blank=True, null=True)
    mailed = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Apinform'


class Apname(models.Model):
    ap_oid = models.CharField(max_length=60, blank=True, null=True)
    ap_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Apname'


class Location(models.Model):
    ap_oid = models.CharField(max_length=60, blank=True, null=True)
    ap_location = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Location'


class Status(models.Model):
    ap_oid = models.CharField(max_length=60, blank=True, null=True)
    ap_status = models.CharField(max_length=12, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Status'


class Status1(models.Model):
    ap_oid = models.CharField(max_length=60, blank=True, null=True)
    ap_status = models.CharField(max_length=12, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Status1'

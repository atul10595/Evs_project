# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class BusInstanceTable(models.Model):
    bus_no = models.IntegerField(db_column='BUS_NO', primary_key=True) # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE') # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'BUS_INSTANCE_TABLE'

class StopRouteTable(models.Model):
    bus_stand = models.CharField(db_column='BUS_STAND', max_length=20) # Field name made lowercase.
    bus_no = models.CharField(db_column='BUS_NO', max_length=20) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'STOP_ROUTE_TABLE'

class StopTable(models.Model):
    bus_stand = models.CharField(db_column='BUS_STAND', primary_key=True, max_length=20) # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True) # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'STOP_TABLE'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class EvsServerCheck(models.Model):
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'evs_server_check'

class EvsServerCheck1(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'evs_server_check1'

class EvsServerLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    bus_no = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'evs_server_location'


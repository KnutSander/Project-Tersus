#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RfidConnection(models.Model):
    uid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='UID', to_field="uid", blank=True, null=True)
    sanitizer = models.ForeignKey('SanitizerStation', models.DO_NOTHING, blank=True, null=True)
    time_dispensed = models.DateTimeField(blank=True, null=True)
    time_spent = models.IntegerField(blank=True, null=True)
    volume_used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RFID_connection'


class Achievement(models.Model):
    employee = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'achievement'


class Department(models.Model):
    name = models.TextField(blank=True, null=True)
    goal = models.ForeignKey('Goal', models.DO_NOTHING, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'department'


class Employee(models.Model):
    uid = models.CharField(db_column='UID', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(blank=False, null=False)
    last_name = models.TextField(blank=False, null=False)
    email = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    risk_group = models.ForeignKey('RiskGroup', models.DO_NOTHING, blank=True, null=True)
    sick_day_id = models.IntegerField(blank=True, null=True)
    sick_days_left = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Goal(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    has_been_achieved = models.BooleanField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'goal'


class RiskGroup(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'risk_group'


class SanitizerStation(models.Model):
    name = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    volume_capacity = models.IntegerField(blank=True, null=True)
    volume_remaining = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'sanitizer_station'


class SickLeave(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    covid_related = models.BooleanField(blank=True, null=False)
    day_started = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sick_leave'

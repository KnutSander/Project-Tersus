#databse file
from django.db import models

class DBTable(models.Model):
    timesWashedToday = models.IntegerField(default=0)
    timesWashedMonth = models.IntegerField(default=0)



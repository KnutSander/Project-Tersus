from django.contrib import admin
from CC import models

admin.site.register(models.Employee)
admin.site.register(models.RiskGroup)
admin.site.register(models.RfidConnection)
admin.site.register(models.Achievement)
admin.site.register(models.SickLeave)
admin.site.register(models.Goal)
admin.site.register(models.SanitizerStation)
admin.site.register(models.Department)
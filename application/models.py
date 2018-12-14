from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
import django
import datetime

class patient(models.Model):
    nameP = models.CharField(max_length=128)

    def __str__(self):
        return self.nameP

class doctor(models.Model):
    nameD = models.CharField(max_length = 128)
    def __str__(self):
        return self.nameD
class prescription(models.Model):
    doctorId = models.ForeignKey(doctor, on_delete = models.CASCADE)
    patientId = models.ForeignKey(patient, on_delete = models.CASCADE)

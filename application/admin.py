# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from application.models import patient, doctor, prescription
# Register your models here.

class patientAdmin(admin.ModelAdmin):
    list_display = ['nameP']

class doctorAdmin(admin.ModelAdmin):
	list_display = ['nameD']

class prescriptionAdmin(admin.ModelAdmin):
	list_display = ['doctorId', 'patientId']

admin.site.register(patient, patientAdmin)
admin.site.register(doctor, doctorAdmin)
admin.site.register(prescription, prescriptionAdmin)

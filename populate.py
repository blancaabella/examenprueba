#populate database
# This code has to be placed in a file within the
# data/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# so let's call it populate.py. Another thing that has to be done
# is creating __init__.py files in both the management and commands
# directories, because these have to be Python packages.
#
# execute python manage.py  populate


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SampleTest.settings')

import django
django.setup()

import random

from application.models import patient, doctor, prescription
#models
# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly

patient.objects.all().delete()
doctor.objects.all().delete()
prescription.objects.all().delete()


# aqui quiero 4 docotors
for i in range(1, 5):
    d = doctor.objects.get_or_create(nameD = 'doctor' + str(i))[0]
    d.save()
#aqui quiero 2 patients
for i in range(1, 3):
    p = patient.objects.get_or_create(nameP = 'patient' + str(i))[0]
    p.save()

l=[(1, 1, 1), (2, 2, 1), (3, 1, 2), (4, 2, 2), (5, 3, 2)]
#aqui quiero 5 prescriptions
for i in range(1,len(l)+1):
    try:
        d = doctor.objects.get(id=l[i-1][1])
    except doctor.DoesNotExist:
        print "doctor with id = " + str(l[i-1][1]) + "does nos exist"
    try:
        p = patient.objects.get(id = l[i-1][2])
    except patient.DoesNotExist:
        print "patient with id = "+ str(l[i-1][2]) + "does nos exist"
    pr = prescription.objects.get_or_create(id = l[i-1][0], doctorId = d ,patientId = p )[0]
    pr.save()

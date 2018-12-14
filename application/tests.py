from unittest import TestCase
from django.test import Client
from application.models import patient, doctor, prescription
from application.management.commands.populate import Command
from django.urls import reverse
from django.db.models import Q
import sys

#execute: python manage.py test find.tests.FindTests.testNAME

#very basis model testing, we just check the objects exists
# returns all  workflows
#DO NOT MODIFIED ANYTHING BELLOW THIS POINT
class ApplicationTests(TestCase):
    def setUp(self):
        # The test client is a Python class that acts as a dummy Web browser
        self._client   = Client()

        # populate database
        self.populate = Command()
        self.populate.handle()


        patient.objects.all().delete()
        doctor.objects.all().delete()
        prescription.objects.all().delete()

    def test1(self): #CHECK
        #firts check all workflows
        this_function_name = sys._getframe().f_code.co_name
        print ("executing: %s" % this_function_name)
        # WORKFLOW_LIST returns all  workflows
        # If you set follow = True the client will follow any redirects
        d = doctor.objects.get_or_create(id = 1, nameD = 'doctor1')
        p = patient.objects.get_or_create(id =1. nameP = 'patient1')
        pr = prescription.objects.get_or_create(id = 1, doctorId = d, patientId = p)
        pr = prescription.objects.get_or_create(id = 2, doctorId = d, patientId = p)
        pr = prescription.objects.get_or_create(id = 3, doctorId = d, patientId = p)
        pr = prescription.objects.get_or_create(id = 4, doctorId = d, patientId = p)


        response = self._client.get(reverse('show_prescription'),
                                    follow=True)
        # Check that all categories and workflow are in the returned page
        prescription = prescription.objects.all()
        self.assertEqual(3, len(prescription))

        # if pagination implemented fill free to use
        # for workflow in workflows[:10]:
        for workflow in workflows:
            self.assertIn(prescription.doctorId, str(response.content))
            print ("    assert: %s"%prescription.doctorId)

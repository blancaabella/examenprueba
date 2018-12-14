# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from application.models import prescription, doctor, patient
import json
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.conf import settings
import urllib
import urllib2
from django.contrib import messages
# Create your views here.
def show_prescription(request):
    # jsonFlag == True -> return html code
    #          == False -> return dict as json
    #             esta opcion (nos ser ́a  ́util en el futuro)
    # YOUR CODE GOES HERE
    # queries that fill, category, categories, workflows
    # and error
    p = prescription.objects.all()
    _dict={'prescription': p[len(p)-3:]}
    return render(request, 'prescription.html', _dict)

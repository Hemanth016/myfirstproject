# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def datetimeinfo(request):
    date=datetime.datetime.now()
    msg='hello guest!!'

    h=int(date.strftime('%H'))
    if h<12:
        msg +='morning'
    elif h<16:
        msg +='afternoon'
    elif h<21:
        msg +='evening'
    else:
        msg='hello guest !!!!!'

    msg=msg+'<h1>now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)

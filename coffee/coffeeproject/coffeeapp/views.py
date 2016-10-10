from django.shortcuts import render, HttpResponse
from django.utils.html import escape
from django.http import JsonResponse
import datetime

import simplejson as json

# Create your views here.
def index(request):
    context = {
        'page_name':"Home",
        'content':"Hello World"
        }
    return render(request,'formexample.html',context)

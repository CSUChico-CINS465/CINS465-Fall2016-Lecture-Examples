from django.shortcuts import render, HttpResponse
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required

import simplejson as json

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    context = {
        'page_name':"Home",
        'content':"Hello World"
        }
    return render(request,'home.html',context)

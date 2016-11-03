from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.utils.html import escape
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required

import simplejson as json
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.
#@login_required(login_url="/login/")
def index(request):
    context = {
        'page_name':"Home",
        'content': Blog.objects.all()[:10]
        }
    return render(request,'home.html',context)


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            print(login(request, user))
            return HttpResponseRedirect('/')

    else:
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

@login_required(login_url="/login/")
def create_blog_post(request):
    if request.method=='POST':
        #print("HAHAHAHA")
        form = blog_entry(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect('/')
    else:
        form = blog_entry()
    context = {
        'form':form
    }
    return render(request,'blogform.html',context)

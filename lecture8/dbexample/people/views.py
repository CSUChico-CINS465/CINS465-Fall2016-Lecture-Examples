from django.shortcuts import render

from .models import Student

# Create your views here.

def index(request):
    listOfStudents = Student.objects.all()
    context = { 'page_name':"List Site", "list":listOfStudents}
    return render(request,'list.html',context)

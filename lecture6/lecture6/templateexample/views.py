from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'page_name':"List Site", "list":[1,2,3,4,5,6,7]}
    return render(request,'list.html',context)

from django.shortcuts import render , HttpResponse
from .models import Employee

# Create your views here.
# def homepage(request):
#     # print(request)
#     print(request.method,request.user)
#     return HttpResponse("hello")


#client----server

def homepage(request):
    # print(request)
    # print(request.method,request.user)
    emps= Employee.objects.all()
    return render(request,'home.html',{"name":"shradha Bidwai","all_emps":emps})


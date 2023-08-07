from django.shortcuts import render

# Create your views here.

def Dashbaord(request):
    return render(request, 'base.html')
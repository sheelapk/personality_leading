from django.shortcuts import render
from contact.models import *
from django.http import *

def data(request):
    obj = user.objects.all()
    return render(request, 'index1.html',{'obj':obj})
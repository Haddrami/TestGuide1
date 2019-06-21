from django.http import HttpResponse
from django.http import request
from django.shortcuts import render

# Create your views here.
def myindex(request):
    return render(request,"guideEnseignement/index.html")
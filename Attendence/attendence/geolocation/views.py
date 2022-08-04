from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json

# Create your views here.
def home(request):
    return render(request, 'geolocation/home.html')

def check(request):
    coords = [i.json() for i in userDetail.objects.all()]
    return HttpResponse(json.dumps(coords), content_type = "application/json")
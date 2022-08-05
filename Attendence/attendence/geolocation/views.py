from enum import unique
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'geolocation/home.html')

def check(request):

    coords = list(userDetail.objects.filter(fld_user_id = 1).values_list('fld_user_id','fld_latitude','fld_longitude','fld_device_info'))
    context = {
        'points' : coords
    }
    return render(request, 'geolocation/check.html', context)
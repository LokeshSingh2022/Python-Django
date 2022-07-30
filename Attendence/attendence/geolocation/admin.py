from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('Id','user_Id','Latitude','Longitude','created_DateTime')
    ordering = ('Id',)


# Register your models here.
admin.site.register(userDetail, UserAdmin)
from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'fld_id',
        'fld_user_id','fld_latitude','fld_longitude',
        'fld_device_info','fld_ip_address','visit_id',
        'auto_check_out','fld_is_active','fld_is_delete',
        'fld_date','fld_time','fld_created_datetime')
    ordering = ('fld_id',)


# Register your models here.
admin.site.register(userDetail, UserAdmin)
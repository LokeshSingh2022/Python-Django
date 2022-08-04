from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

class userDetail(models.Model):

    fld_id = models.BigAutoField(primary_key=True)
    fld_user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # use your "user" model here
    fld_latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)], blank=True, null=True)
    fld_longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], blank=True, null=True)
    fld_device_info = models.CharField(max_length=100, blank=True, null=True)
    fld_ip_address = models.CharField(max_length=100, blank=True, null=True)
    visit_id = models.CharField(max_length=50, blank=True, null=True, db_column="fld_visit_id")
    auto_check_out = models.BooleanField(default=False, db_column="fld_auto_check_out")
    fld_is_active = models.BooleanField(default=True)
    fld_is_delete = models.BooleanField(default=False)
    fld_date = models.DateField(blank=True, null=True)
    fld_time = models.TimeField(blank=True, null=True)
    fld_created_datetime = models.DateTimeField(auto_now_add=True)

    def json(self):
        return {
            'fld_latitude' : self.fld_latitude,
            'fld_longitude' : self.fld_longitude,
        }

    class Meta:
        managed = True
        db_table = 'userDetail'
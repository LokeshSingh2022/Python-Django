from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userDetail(models.Model):
    Id = models.BigAutoField(primary_key=True)
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE,default = None)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    created_DateTime = models.DateTimeField(auto_now_add=True, null=True)


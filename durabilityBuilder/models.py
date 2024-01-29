from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=128)


class Program(models.Model):
    description = models.CharField(max_length=128)
    duration_days = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    display_order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)




from django.db import models
from django.contrib.auth.models import User


class PartHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    part1 = models.IntegerField(default=0)
    part2 = models.IntegerField(default=0)
    part3 = models.IntegerField(default=0)
    part4 = models.IntegerField(default=0)
    part5 = models.IntegerField(default=0)
    part6 = models.IntegerField(default=0)
    part7 = models.IntegerField(default=0)
    part8 = models.IntegerField(default=0)

    def __str__(self):
        return self.user


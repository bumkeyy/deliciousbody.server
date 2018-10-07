from django.db import models
from django.contrib.auth.models import User


class PartHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    part1 = models.IntegerField(default=0, verbose_name='목 / 어깨')
    part2 = models.IntegerField(default=0, verbose_name='가슴')
    part3 = models.IntegerField(default=0, verbose_name='복부 / 허리')
    part4 = models.IntegerField(default=0, verbose_name='허벅지 / 무릎')
    part5 = models.IntegerField(default=0, verbose_name='종아리 / 발목')
    part6 = models.IntegerField(default=0, verbose_name='팔 / 손목')
    part7 = models.IntegerField(default=0, verbose_name='등')
    part8 = models.IntegerField(default=0, verbose_name='엉덩이')

    def __str__(self):
        return self.user


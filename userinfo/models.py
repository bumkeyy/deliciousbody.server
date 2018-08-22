from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField



class UserInfo(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(200)])
    is_man = models.BooleanField(default=True) # True is man
    activity_level = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(2)]) # 0, 1, 2
    interested_part = ArrayField(models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)]),
                                 size=8)
    weekdays_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekdays_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekend_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekend_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)])
    comment = models.CharField(max_length=12)
    avatar = models.ImageField(unique=False, default='/impyage.jpg')
    favorite_list = ArrayField(models.IntegerField())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_push = models.BooleanField(default=True)

    def __str__(self):
        return self.name
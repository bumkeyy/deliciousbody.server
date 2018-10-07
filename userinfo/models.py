from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default="name", max_length=10)
    age = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(200)])
    is_man = models.BooleanField(default=True) # True is man
    activity_level = models.IntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(3)]) # 0, 1, 2
    interested_part = models.CharField(default="1;2;3", max_length=20)
    comment = models.CharField(default="comment", max_length=30, blank=True)
    avatar = models.CharField(default=".", max_length=100)
    favorite_list = models.CharField(default="1;2;3", max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    weekdays_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekdays_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekend_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekend_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)])
    is_push_weekdays = models.BooleanField(default=True)
    is_push_weekend = models.BooleanField(default=True)

    is_subscription = models.BooleanField(default=True)

    phone_model = models.CharField(max_length=300, blank=True)
    push_id = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
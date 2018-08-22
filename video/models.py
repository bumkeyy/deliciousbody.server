from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator

class Video(models.Model):
    video_name = models.CharField(max_length=30)
    level = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(2)])
    part = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])
    time = models.IntegerField()
    description = models.TextField(max_length=300)
    video_url = models.TextField(validators=[URLValidator()])
    thumbnail_url = models.TextField(validators=[URLValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
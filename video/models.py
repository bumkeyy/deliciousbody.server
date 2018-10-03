from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator

class Video(models.Model):
    video_name = models.CharField(max_length=50)
    video_id = models.IntegerField(default=0)
    level = models.IntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(3)])
    part1 = models.BooleanField(default=True)
    part2 = models.BooleanField(default=False)
    part3 = models.BooleanField(default=False)
    part4 = models.BooleanField(default=False)
    part5 = models.BooleanField(default=False)
    part6 = models.BooleanField(default=False)
    part7 = models.BooleanField(default=False)
    part8 = models.BooleanField(default=False)
    time = models.IntegerField()
    description = models.TextField(max_length=300)
    video_url = models.TextField(validators=[URLValidator()])
    #video_file = models.FileField(upload_to="video/%Y/%m/%d")
    #video_thumbnail = models.ImageField(unique=False, default='/profile/default.png')
    video_file = models.TextField(validators=[URLValidator()])
    video_thumbnail = models.TextField(validators=[URLValidator()])
    with_list = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '(%d) %s' % (self.video_id, self.video_name)
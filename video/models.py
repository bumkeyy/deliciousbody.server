from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator


class Video(models.Model):
    video_name = models.CharField(max_length=50)
    video_id = models.IntegerField(default=0, unique=True)
    level = models.IntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(3)])

    main_part = models.IntegerField(default=0, verbose_name="주 운동부위")
    sub_part = models.IntegerField(default=0, verbose_name="부 운동부위")

    time = models.IntegerField()
    description = models.TextField(max_length=300)
    video_url = models.TextField(validators=[URLValidator()], blank=True, null=True)
    video_file = models.FileField(upload_to="video/")
    video_thumbnail = models.ImageField(upload_to="video_thumbnail/")
    with_list = models.ForeignKey('video_list.VideoList', on_delete=models.CASCADE, blank=True, null=True, related_name='with_list')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '(%d) %s' % (self.video_id, self.video_name)

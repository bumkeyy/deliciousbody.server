from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator


class Video(models.Model):
    video_name = models.CharField(max_length=50)
    video_id = models.IntegerField(default=0)
    level = models.IntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(3)])
    part1 = models.BooleanField(default=True, verbose_name='목 / 어깨')
    part2 = models.BooleanField(default=False, verbose_name='가슴')
    part3 = models.BooleanField(default=False, verbose_name='복부 / 허리')
    part4 = models.BooleanField(default=False, verbose_name='허벅지 / 무릎')
    part5 = models.BooleanField(default=False, verbose_name='종아리 / 발목')
    part6 = models.BooleanField(default=False, verbose_name='팔 / 손목')
    part7 = models.BooleanField(default=False, verbose_name='등')
    part8 = models.BooleanField(default=False, verbose_name='엉덩이')
    time = models.IntegerField()
    description = models.TextField(max_length=300)
    video_url = models.TextField(validators=[URLValidator()])
    video_file = models.TextField(validators=[URLValidator()])
    video_thumbnail = models.TextField(validators=[URLValidator()])
    with_list = models.ForeignKey('video_list.VideoList', on_delete=models.CASCADE, blank=True, null=True, related_name='with_list')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '(%d) %s' % (self.video_id, self.video_name)
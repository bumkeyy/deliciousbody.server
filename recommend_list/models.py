from django.db import models
from django.core.validators import URLValidator

class RecommendList(models.Model):
    list_id = models.IntegerField()
    list_name = models.CharField(max_length=30)
    list_count = models.IntegerField()
    time = models.IntegerField(verbose_name="time(sec)")
    list_image = models.ImageField(upload_to="recommend_image/")

    videolist = models.ForeignKey('video_list.VideoList', on_delete=models.CASCADE, related_name = 'videolist', null=True, blank=True)
    #video_list = models.ForeignKey('video.Video', on_delete=models.CASCADE, related_name = 'video_list', null=True, blank=True)

    part0 = models.BooleanField(default=True, verbose_name='전신')
    part1 = models.BooleanField(default=False, verbose_name='목 / 어깨')
    part2 = models.BooleanField(default=False, verbose_name='가슴')
    part3 = models.BooleanField(default=False, verbose_name='복부 / 허리')
    part4 = models.BooleanField(default=False, verbose_name='허벅지 / 무릎')
    part5 = models.BooleanField(default=False, verbose_name='종아리 / 발목')
    part6 = models.BooleanField(default=False, verbose_name='팔 / 손목')
    part7 = models.BooleanField(default=False, verbose_name='등')
    part8 = models.BooleanField(default=False, verbose_name='엉덩이')


    def __str__(self):
        return '(%d) %s' % (self.list_id, self.list_name)













from django.db import models
from django.core.validators import URLValidator

class RecommendList(models.Model):
    list_id = models.IntegerField()
    list_name = models.CharField(max_length=30)
    list_count = models.IntegerField()
    time = models.IntegerField()
    list_image = models.TextField(validators=[URLValidator()])

    video_list = models.ForeignKey('video_list.VideoList', on_delete=models.CASCADE, related_name = 'video_list', null=True, blank=True)

    part1 = models.BooleanField(default=True)
    part2 = models.BooleanField(default=False)
    part3 = models.BooleanField(default=False)
    part4 = models.BooleanField(default=False)
    part5 = models.BooleanField(default=False)
    part6 = models.BooleanField(default=False)
    part7 = models.BooleanField(default=False)
    part8 = models.BooleanField(default=False)


    def __str__(self):
        return '(%d) %s' % (self.list_id, self.list_name)













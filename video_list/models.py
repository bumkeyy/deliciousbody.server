from django.db import models


class VideoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=30)

    video1 = models.ForeignKey('video.Video', on_delete=models.CASCADE, blank=True, null=True, related_name='video1')
    video2 = models.ForeignKey('video.Video', on_delete=models.CASCADE, blank=True, null=True, related_name='video2')
    video3 = models.ForeignKey('video.Video', on_delete=models.CASCADE, blank=True, null=True, related_name='video3')
    video4 = models.ForeignKey('video.Video', on_delete=models.CASCADE, blank=True, null=True, related_name='video4')
    video5 = models.ForeignKey('video.Video', on_delete=models.CASCADE, blank=True, null=True, related_name='video5')

    def __str__(self):
        return '(%d) %s' % (self.list_id, self.list_name)


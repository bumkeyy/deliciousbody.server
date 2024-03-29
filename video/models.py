from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator


class Video(models.Model):
    video_name = models.CharField(max_length=50)
    video_id = models.IntegerField(default=0, unique=True)
    level = models.IntegerField(default=2, 
    validators=[MinValueValidator(1), MaxValueValidator(3)],
    choices=(
        (1, '저'),
        (2, '중'),
        (3, '고'),),
    verbose_name="운동 수준")
    main_part = models.IntegerField(
        default=0, 
        verbose_name="주 운동부위",
        choices=(
            (0, '전신'),#
            (1, '목 / 어깨'),#
            (2, '가슴'),#
            (3, '복부 / 허리'),#
            (4, '허벅지 / 무릎'),#
            (5, '종아리 / 발목'),#
            (6, '팔 / 손목'),
            (7, '등'),
            (8, '엉덩이')
        ))
    sub_part = models.IntegerField(
        default=0, 
        verbose_name="부 운동부위", 
        null=True,
        choices=(
            (0, '전신'),
            (1, '목 / 어깨'),
            (2, '가슴'),
            (3, '복부 / 허리'),
            (4, '허벅지 / 무릎'),
            (5, '종아리 / 발목'),
            (6, '팔 / 손목'),
            (7, '등'),
            (8, '엉덩이'),
            (9, '없음')
        ))

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


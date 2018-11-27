from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=30, verbose_name="이름")
    age = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(200)], verbose_name="나이")
    is_man = models.BooleanField(default=True, verbose_name="남자 유무") # True is man
    activity_level = models.IntegerField(
            default=2, 
            validators=[MinValueValidator(1), MaxValueValidator(3)], 
            choices=(
            (1, '저'),
            (2, '중'),
            (3, '고'),),
            verbose_name="활동 수준") # 0, 1, 2
    interested_part = models.CharField(default="1;2;3", max_length=20, verbose_name="관심 부위")
    comment = models.CharField(default="comment", max_length=30, blank=True, verbose_name="동기 부여 멘트")
    avatar = models.CharField(max_length=100, blank=True, null=True, verbose_name="프로필 사진")
    favorite_list = models.CharField(default="1;2;3", max_length=1000, verbose_name="좋아요 리스트")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    weekdays_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="주중 알림 시작 시간")
    weekdays_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="주중 알림 종료 시간")
    weekend_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="주말 알림 시작 시간")
    weekend_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)], verbose_name="주말 알림 종료 시간")
    is_push_weekdays = models.BooleanField(default=True, verbose_name="주중 알림")
    is_push_weekend = models.BooleanField(default=True, verbose_name="주말 알림")

    is_subscription = models.BooleanField(default=True)

    phone_model = models.CharField(max_length=300, blank=True, null=True)
    push_id = models.CharField(max_length=300, blank=True, null=True)

    part0 = models.IntegerField(default=0, verbose_name='전신')
    part1 = models.IntegerField(default=0, verbose_name='목 / 어깨')
    part2 = models.IntegerField(default=0, verbose_name='가슴')
    part3 = models.IntegerField(default=0, verbose_name='복부 / 허리')
    part4 = models.IntegerField(default=0, verbose_name='허벅지 / 무릎')
    part5 = models.IntegerField(default=0, verbose_name='종아리 / 발목')
    part6 = models.IntegerField(default=0, verbose_name='팔 / 손목')
    part7 = models.IntegerField(default=0, verbose_name='등')
    part8 = models.IntegerField(default=0, verbose_name='엉덩이')


    # push info
    prev_video_id = models.IntegerField(default = 0)
    next_video_id = models.IntegerField(default = 0)
    weekdays_prev_hour = models.IntegerField(default=0)
    weekdays_next_hour = models.IntegerField(default=0)
    weekend_prev_hour = models.IntegerField(default = 0)
    weekend_next_hour = models.IntegerField(default = 0)
    weekdays_push_list = models.CharField(default='0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27', max_length=1000)
    weekend_push_list = models.CharField(default='0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27', max_length=1000)


    def __str__(self):
        return self.name


def on_post_save_for_userinfo(sender, **kwargs):
    if kwargs['created']:
        userinfo = kwargs['instance']
        name = User.objects.filter(id=userinfo.user.id).values_list('first_name', flat=True).get()
        if name : 
                userinfo.name = name
                userinfo.save()

post_save.connect(on_post_save_for_userinfo, sender=UserInfo)




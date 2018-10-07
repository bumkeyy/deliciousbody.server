from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import random
from userinfo.models import UserInfo
from video.models import Video


class Push(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weekdays_push_list = models.CharField(default='0', max_length=500)
    weekend_push_list = models.CharField(default='0', max_length=500)
    weekdays_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekdays_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekend_start = models.IntegerField(default=8, validators=[MinValueValidator(0), MaxValueValidator(24)])
    weekend_end = models.IntegerField(default=22, validators=[MinValueValidator(0), MaxValueValidator(24)])
    video_id = models.IntegerField()
    next_hour = models.IntegerField()


    def save(self, *args, **kwargs):
        if not self.pk:
            weekdays_list = list()
            weekend_list = list()
            for i in range(self.weekdays_start, self.weekdays_end + 1):
                weekdays_list.append(i)
                weekdays_list *= 5
            for i in range(self.weekend_start, self.weekend_end + 1):
                weekend_list.append(i)
                weekend_list *= 5
            self.weekdays_push_list = str(weekdays_list)
            self.weekend_push_list = str(weekend_list)
        super(Push, self).save(*args, **kwargs)


    def push_check(self):
        weekno = datetime.datetime.today().weekday()
        # weekdays
        if weekno < 5:
            # 알람 시간일 경우
            if datetime.today().hour == self.next_hour :
                tmp_hour = random.choice(self.weekdays_push_list)
                while self.next_hour > tmp_hour:
                    tmp_hour = random.choice(self.weekdays_push_list)

                # 전 시간 다음이라면 새로운 운동 추천
                if self.next_hour < tmp_hour :
                    video_id = search_video(self)
                    self.next_hour = tmp_hour

                    '''
                    fcm push
                    '''
                # 마지막 시간 일 경우
                elif self.next_hour == self.weekdays_end :
                    video_id = search_video(self)
                    self.next_hour = self.weekdays_start

                    '''
                    fcm push
                    '''

            # 해당 시간이 아니면 패스
            else:
                pass
        # weekend
        else:
            if datetime.today().hour == self.next_hour :
                tmp_hour = random.choice(self.weekend_push_list)
                while self.next_hour > tmp_hour:
                    tmp_hour = random.choice(self.weekend_push_list)

                # 전 시간 다음이라면 새로운 운동 추천
                if self.next_hour < tmp_hour :
                    video_id = search_video(self)
                    self.next_hour = tmp_hour
                    # fcm_test
                # 마지막 시간 일 경우
                elif self.next_hour == self.weekend_end :
                    video_id = search_video(self)
                    self.next_hour = self.weekend_start
                    # fcm_test

            # 해당 시간이 아니면 패스
            else:
                pass

def search_video(self):
    interest = UserInfo.objects.filter(user=self.request.user).values_list('interested_part', flat=True).get(pk=1)
    interest_list = interest.split(';')
    all_video = Video.objects.all()
    v_list = Video.objects.none()

    if '1' in interest_list:
        v_list = all_video.filter(part1=True)
    if '2' in interest_list:
        v_list = v_list | all_video.filter(part2=True)
    if '3' in interest_list:
        v_list = v_list | all_video.filter(part3=True)
    if '4' in interest_list:
        v_list = v_list | all_video.filter(part4=True)
    if '5' in interest_list:
        v_list = v_list | all_video.filter(part5=True)
    if '6' in interest_list:
        v_list = v_list | all_video.filter(part6=True)
    if '7' in interest_list:
        v_list = v_list | all_video.filter(part7=True)
    if '8' in interest_list:
        v_list = v_list | all_video.filter(part8=True)

    v_index = self.Push.video_id
    while (v_index == self.Push.video_id):
        v_index = random.choice(v_list).values_list('video_id', flat=True).get(pk=1)
    return v_index












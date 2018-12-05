import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.debug'

from userinfo.models import UserInfo
from video.models import Video
from video.serializers import VideoSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime
import random
import requests
import json
from django.conf import settings
from django.http import HttpResponse
from pytz import timezone
from django.db.models import Q


def send_fcm(push_id, video_obj):
    # fcm 푸시 메세지 요청 주소
    url = 'https://fcm.googleapis.com/fcm/send'

    # 인증 정보(서버 키)를 헤더에 담아 전달
    headers = {
        'Authorization': 'key='+ getattr(settings, 'SERVER_KEY'),
        'Content-Type': 'application/json; UTF-8',
    }

    content = {
        'to': push_id,
        'notification': {
            #'title' : 'push',
            'body': '맛있는 운동이 도착했어요.'
        },
        'data': {
            'video' : VideoSerializer(video_obj).data
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(content))
    print(response)



# test
def send_fcm_test(self):

    # fcm 푸시 메세지 요청 주소
    url = 'https://fcm.googleapis.com/fcm/send'

    obj = get_object_or_404(UserInfo, name='기범')
    video_obj = get_object_or_404(Video, video_id = 3)

    # 인증 정보(서버 키)를 헤더에 담아 전달
    headers = {
        'Authorization': 'key='+ getattr(settings, 'SERVER_KEY'),
        'Content-Type': 'application/json; UTF-8',
    }

    content = {
        'to': obj.push_id,
        'notification': {
            'title' : 'deliciousbody test',
            'body': 'deliciousbody test'
        },
        'data': {
            'video' : VideoSerializer(video_obj).data
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(content))
    return HttpResponse(response)

def recommend_video(obj):
    interest = obj.interested_part
    i_list = interest.split(';')

    while True:
        part_id = random.choice(i_list)
        # 팔 / 손목이거나 등이면 전신으로 수정 (조치)
        if part_id == '6' or part_id == '7':
            part_id = 0
        # 주 운동부위와 부 운동 부위 전부 검색
        # 운동수가 적기 때문에
        v_obj = Video.objects.filter(Q(main_part=part_id) | Q(sub_part=part_id)).order_by('?').first()
        #print(f'v_obj : {v_obj}')
        '''
        if v_obj is None:
            v_obj = Video.objects.filter(sub_part=part_id).order_by('?').first()
        '''
        if v_obj.video_id != obj.prev_video_id:
            return v_obj


def push_task(request):
    all_userinfo = UserInfo.objects.all()
    # 모든 인스턴스 검사
    for obj in all_userinfo:
        try:
            weekno = datetime.now(timezone('Asia/Seoul')).weekday()
            # weekdays
            if weekno < 5 and obj.is_push_weekdays :
                # 알람 시간일 경우
                if datetime.now(timezone('Asia/Seoul')).hour == obj.weekdays_next_hour:
                    # 다음 알람시간 선택
                    while True:
                        weekdays_push_list = obj.weekdays_push_list.split(',')
                        tmp_hour = int(random.choice(weekdays_push_list))

                        # 전 시간 3시간 이내라면 새로운 운동 추천
                        if obj.weekdays_next_hour < tmp_hour and obj.weekdays_next_hour >= tmp_hour - 3:
                            # 마지막 시간보다 크다면
                            if tmp_hour > obj.weekdays_end or tmp_hour - 3 > obj.weekdays_end :
                                obj.weekdays_prev_hour = obj.weekdays_next_hour
                                obj.weekdays_next_hour = obj.weekdays_start

                                # 설정해 놓은 운동 부위가 있다면
                                if obj.interested_part : 
                                    # 추천 운동 정함
                                    obj.prev_video_id = obj.next_video_id
                                    video_obj = recommend_video(obj)
                                    obj.next_video_id = video_obj.video_id
                                    if not obj.push_id:
                                        break
                                    send_fcm(obj.push_id, video_obj)
                                obj.save()
                                break

                            # 24보다 클 경우 첫 시간에 운동 할당
                            if tmp_hour > 24 :
                                obj.weekdays_prev_hour = obj.weekdays_next_hour
                                obj.weekdays_next_hour = obj.weekdays_start

                                # 설정해 놓은 운동 부위가 있다면
                                if obj.interested_part : 
                                    # 추천 운동 정함
                                    obj.prev_video_id = obj.next_video_id
                                    video_obj = recommend_video(obj)
                                    obj.next_video_id = video_obj.video_id
                                    if not obj.push_id:
                                        break
                                    send_fcm(obj.push_id, video_obj)
                                obj.save()
                                break
                            else :
                                obj.weekdays_prev_hour = obj.weekdays_next_hour
                                if tmp_hour == 24:
                                    tmp_hour = 0
                                obj.weekend_next_hour = tmp_hour

                                # 설정해 놓은 운동 부위가 있다면
                                if obj.interested_part : 
                                    # 추천 운동 정함
                                    obj.prev_video_id = obj.next_video_id
                                    video_obj = recommend_video(obj)
                                    obj.next_video_id = video_obj.video_id
                                    if not obj.push_id:
                                        break
                                    send_fcm(obj.push_id, video_obj)
                                    if not obj.push_id:
                                        break
                                obj.save()
                                break

                # 알람 시간이 아닐 경우 그냥 pass
                else :
                    pass
                pass
            # weekend
            elif weekno >= 5 and obj.is_push_weekend :
                # 알람 시간일 경우
                if datetime.now(timezone('Asia/Seoul')).hour == obj.weekend_next_hour:
                    # 다음 알람시간 선택
                    while True:
                        weekend_push_list = obj.weekend_push_list.split(',')
                        tmp_hour = int(random.choice(weekend_push_list))
                        # 전 시간 3시간 이내라면 새로운 운동 추천
                        if obj.weekend_next_hour < tmp_hour and obj.weekend_next_hour >= tmp_hour - 3:
                            # 마지막 시간보다 크다면
                            if tmp_hour > obj.weekend_end or tmp_hour - 3 > obj.weekend_end:
                                obj.weekend_prev_hour = obj.weekend_next_hour
                                obj.weekend_next_hour = obj.weekend_start
                                # 설정해 놓은 운동 부위가 있다면
                                if obj.interested_part : 
                                    # 추천 운동 정함
                                    obj.prev_video_id = obj.next_video_id
                                    video_obj = recommend_video(obj)
                                    obj.next_video_id = video_obj.video_id
                                    if not obj.push_id:
                                        break
                                    send_fcm(obj.push_id, video_obj)
                                obj.save()
                                break

                            # 24보다 클 경우 첫 시간에 운동 할당
                            if tmp_hour > 24:
                                obj.weekend_prev_hour = obj.weekend_next_hour
                                obj.weekend_next_hour = obj.weekend_start
                                # 설정해 놓은 운동 부위가 있다면
                                if obj.interested_part : 
                                    # 추천 운동 정함
                                    obj.prev_video_id = obj.next_video_id
                                    video_obj = recommend_video(obj)
                                    obj.next_video_id = video_obj.video_id
                                    if not obj.push_id:
                                        break
                                    send_fcm(obj.push_id, video_obj)
                                obj.save()
                                break
                            else:
                                obj.weekend_prev_hour = obj.weekend_next_hour
                                if tmp_hour == 24:
                                    tmp_hour = 0
                                obj.weekend_next_hour = tmp_hour
                                # 설정해 놓은 운동 부위가 있다면
                                if obj.interested_part : 
                                    # 추천 운동 정함
                                    obj.prev_video_id = obj.next_video_id
                                    video_obj = recommend_video(obj)
                                    obj.next_video_id = video_obj.video_id
                                    if not obj.push_id:
                                        break
                                    send_fcm(obj.push_id, video_obj)
                                obj.save()
                                break
                # 알람 시간이 아닐 경우 그냥 pass
                else:
                    pass
            # not
            else:
                pass

        except UserInfo.DoesNotExist:
            pass
    return HttpResponse("Push time : %d" % (datetime.now(timezone('Asia/Seoul')).hour))

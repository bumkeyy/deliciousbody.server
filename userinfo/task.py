from userinfo.models import UserInfo
from video.models import Video
from datetime import datetime
import random
import requests
import json, os
from django.conf import settings

SERVER_KEY = getattr(settings, 'SERVER_KEY')

def send_fcm(push_id, video_id):
    # fcm 푸시 메세지 요청 주소
    url = 'https://fcm.googleapis.com/fcm/send'

    # 인증 정보(서버 키)를 헤더에 담아 전달
    headers = {
        'Authorization': 'key= '+ SERVER_KEY,
        'Content-Type': 'application/json; UTF-8',
    }

    data = {
        'to': push_id,
        'data': {
            'message_body': video_id
        },
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response)

def recommend_video(pk, prev_video_id):
    interest = UserInfo.objects.filter(pk=pk).values_list('interested_part', flat=True).get()
    i_list = interest.split(';')

    while True:
        part_id = random.choice(i_list)
        v_obj = Video.objects.filter(main_part=part_id).order_by('?').first()
        if v_obj.video_id != prev_video_id:
            return v_obj.video_id


def push_task():
    num = UserInfo.objects.all().count()
    i = 0
    pk = 1
    # 모든 인스턴스 검사
    while i <= num :

        try:
            obj = UserInfo.objects.get(pk=pk)
            i += 1
            weekno = datetime.today().weekday()
            # weekdays
            if weekno < 5 and obj.is_push_weekdays :
                # 알람 시간일 경우
                if datetime.today().hour == obj.next_hour:
                    # 다음 알람시간 선택
                    while True:
                        weekdays_push_list = obj.weekdays_push_list.split(',')
                        tmp_hour = random.choice(weekdays_push_list)
                        # 전 시간 3시간 이내라면 새로운 운동 추천
                        if obj.next_hour < tmp_hour and obj.next_hour >= tmp_hour - 3:
                            # 마지막 시간보다 크다면
                            if tmp_hour > obj.weekdays_end or tmp_hour - 3 > obj.weekdays_end :
                                obj.prev_hour = obj.next_hour
                                obj.next_hour = obj.weekdays_start
                                # 추천 운동 정함
                                obj.prev_video_id = obj.next_video_id
                                obj.next_video_id = recommend_video(pk, obj.prev_video_id)
                                send_fcm(obj.push_id, obj.next_video_id)
                                break

                            # 24보다 클 경우 첫 시간에 운동 할당
                            if tmp_hour > 24 :
                                obj.prev_hour = obj.next_hour
                                obj.next_hour = obj.weekdays_start
                                # 추천 운동 정함
                                obj.prev_video_id = obj.next_video_id
                                obj.next_video_id = recommend_video(pk, obj.prev_video_id)
                                send_fcm(obj.push_id, obj.next_video_id)
                                break
                            else :
                                obj.prev_hour = obj.next_hour
                                obj.next_hour = tmp_hour
                                # 추천 운동 정함
                                obj.prev_video_id = obj.next_video_id
                                obj.next_video_id = recommend_video(pk, obj.prev_video_id)
                                send_fcm(obj.push_id, obj.next_video_id)
                                break

                # 알람 시간이 아닐 경우 그냥 pass
                else :
                    pass
                pass
            # weekend
            elif weekno > 5 and obj.is_push_weekend :
                # 알람 시간일 경우
                if datetime.today().hour == obj.next_hour:
                    # 다음 알람시간 선택
                    while True:
                        weekend_push_list = obj.weekend_push_list.split(',')
                        tmp_hour = random.choice(weekend_push_list)
                        # 전 시간 3시간 이내라면 새로운 운동 추천
                        if obj.next_hour < tmp_hour and obj.next_hour > tmp_hour - 3:
                            # 마지막 시간보다 크다면
                            if tmp_hour > obj.weekend_end and tmp_hour - 3 >= obj.weekend_end:
                                obj.prev_hour = obj.next_hour
                                obj.next_hour = obj.weekend_start
                                # 추천 운동 정함
                                obj.prev_video_id = obj.next_video_id
                                obj.next_video_id = recommend_video(pk, obj.prev_video_id)
                                send_fcm(obj.push_id, obj.next_video_id)
                                break

                            # 24보다 클 경우 첫 시간에 운동 할당
                            if tmp_hour > 24:
                                obj.prev_hour = obj.next_hour
                                obj.next_hour = obj.weekend_start
                                # 추천 운동 정함
                                obj.prev_video_id = obj.next_video_id
                                obj.next_video_id = recommend_video(pk, obj.prev_video_id)
                                send_fcm(obj.push_id, obj.next_video_id)
                                break
                            else:
                                obj.prev_hour = obj.next_hour
                                obj.next_hour = tmp_hour
                                # 추천 운동 정함
                                obj.prev_video_id = obj.next_video_id
                                obj.next_video_id = recommend_video(pk, obj.prev_video_id)
                                send_fcm(obj.push_id, obj.next_video_id)
                                break

                # 알람 시간이 아닐 경우 그냥 pass
                else:
                    pass
            # not
            else:
                pass

        except UserInfo.DoesNotExist:
            pass
        pk += 1

        if pk > num + 100:
            break



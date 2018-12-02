from rest_framework import status
from rest_framework.test import APITransactionTestCase
from .models import Video
from rest_framework.test import APIClient
import json


# Video Test
class VideoInfoTest(APITransactionTestCase):

    # test 유저 생성 및 video 파일 추가
    def setUp(self):
        self.client = APIClient()
        # user 생성
        url = '/rest-auth/registration/'
        sdata = {'email': 'test@gmail.com', 'password1': '12345678', 'password2': '12345678', 'first_name':'hello'}
        self.client.post(url, sdata, format='json')
        # jwt 토큰 획득
        get_JWT_url = '/api-jwt-auth/'
        jwt_data = {'username': 'hello', 'password': '12345678'}
        jwt_response = self.client.post(get_JWT_url, jwt_data)
        token = json.loads(jwt_response.content.decode('utf-8'))["token"]
        # jwt 토큰 헤더에 등록
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # userinfo 생성
        userinfo_url = '/userinfo/'
        self.client.post(userinfo_url)

        for i in range(0, 9):
            Video.objects.create(video_name='video',
            video_id=i,
            level=1,
            main_part=i,
            sub_part=1,
            time=1,
            description='hello',
            video_url='http://ds.png',
            video_thumbnail='http://ds.png')

    # video 전체 영상 정보
    def _get_video(self):
        url = '/video/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 해당 video 정보 반환
    def _get_id_video(self):
        urlList = list('/video/0/')
        for i in range(0, 9):
            urlList[7] = str(i)
            url = ''.join(urlList)
            response = self.client.get(url)
            get_id = json.loads(response.content.decode('utf-8'))["video_id"]
            self.assertEqual(get_id, i)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 유저가 좋아하는 list 반환
    def _get_flist_video(self):
        url = '/video/like/'
        response = self.client.get(url)
        get_list = json.loads(response.content.decode('utf-8'))

        ll = list()
        for vlist in get_list:
            ll.append(str(vlist['video_id']))
        fll = sorted(set(ll))
        self.assertEqual(['1', '2', '3'], fll)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_main(self):
        print('------------------VideoInfoTest Start------------------')
        self._get_video()
        print('Success : VideoInfoTest_get_video')
        self._get_id_video()
        print('Success : VideoInfoTest_get_id_video')
        self._get_flist_video()
        print('Success : VideoInfoTest_get_flist_video')
        print('')











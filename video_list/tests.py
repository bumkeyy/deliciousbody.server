from rest_framework import status
from rest_framework.test import APITransactionTestCase
from rest_framework.test import APIClient
from .models import VideoList
import json


# Video List Test
class VideoListInfoTest(APITransactionTestCase):

    # test 유저 생성 및 videolist 파일 추가
    def setUp(self):
        self.client = APIClient()
        # user 생성
        url = '/rest-auth/registration/'
        sdata = {'email': 'test@gmail.com', 'password1': '12345678', 'password2': '12345678','first_name':'hello'}
        self.client.post(url, sdata, format='json')
        # jwt 토큰 획득
        get_JWT_url = '/api-jwt-auth/'
        jwt_data = {'username': 'hello', 'password': '12345678'}
        jwt_response = self.client.post(get_JWT_url, jwt_data)
        token = json.loads(jwt_response.content.decode('utf-8'))["token"]
        # jwt 토큰 헤더에 등록
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        for i in range(0, 9):
            VideoList.objects.create(
            list_name='list',
            list_count = 0)

    def _get_videolist(self):
        urlList = list('/videolist/0/')
        for i in range(1, 9):
            urlList[11] = str(i)
            url = ''.join(urlList)
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_main(self):
        print('------------------VideoListInfoTest Start------------------')
        self._get_videolist()
        print('Success : VideoListInfoTest_get_videolist')
        print('')

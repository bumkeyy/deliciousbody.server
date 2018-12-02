from rest_framework import status
from rest_framework.test import APITransactionTestCase
from django.contrib.auth.models import User
from .models import UserInfo
import json
from rest_framework.test import APIClient


# 이메일 계정 테스트
class EmailAccountTest(APITransactionTestCase):

    # 유저 이메일 가입 테스트 (success : 201, failure : 400)
    def _create_user(self):
        url = '/rest-auth/registration/'
        # 성공시
        sdata = {'email':'test@gmail.com', 'password1':'12345678', 'password2':'12345678', 'first_name':'hello'}
        response = self.client.post(url, sdata, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@gmail.com')
        # 실패시
        fdata = {'email': 'aaaaa', 'password1': '123456', 'password2': '123456'}
        response = self.client.post(url, fdata, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # 유저 이메일 로그인 테스트 (success : 200, failure : 400)
    def _login_user(self):
        url = '/rest-auth/login/'
        # 성공시
        sdata = {'email': 'test@gmail.com', 'password': '12345678'}
        response = self.client.post(url, sdata)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 실패시
        fdata = {'email': 'tes@gmail.com', 'password': '12345678'}
        response = self.client.post(url, fdata)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # 유저 비밀번호 찾기 (success : 200, failure : 400)
    def _reset_password_user(self):
        url = '/rest-auth/password/reset/'
        # 성공시
        sdata = {'email': 'test@gmail.com'}
        response = self.client.post(url, sdata)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #실패시
        fdata = {'email': 'tes@gmail.com'}
        response = self.client.post(url, fdata)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 유저 기존 비밀번호 재설정 (success : 200, failure : 400)
    def _change_password_user(self):
        url = '/rest-auth/password/change/'
        get_JWT_url = '/api-jwt-auth/'
        jwt_data = {'username':'hello', 'password':'12345678'}
        jwt_response = self.client.post(get_JWT_url, jwt_data)
        token = json.loads(jwt_response.content.decode('utf-8'))["token"]
        # 성공시
        sdata = {'old_password':'12345678', 'new_password1':'12345677', 'new_password2':'12345677'}
        response = self.client.post(url, sdata, HTTP_AUTHORIZATION='JWT {}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 실패시
        fdata = {'email': 'tes'}
        response = self.client.post(url, fdata, HTTP_AUTHORIZATION='JWT {}'.format(token))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 테스트
    def test_main(self):
        print('------------------EmailAccountTest Start------------------')
        self._create_user()
        print('Success : EmailAccountTest_create_user')
        self._login_user()
        print('Success : EmailAccountTest_login_user')
        self._reset_password_user()
        print('Success : EmailAccountTest_reset_password_user')
        self._change_password_user()
        print('Success : EmailAccountTest_change_password_user')
        print()

# UserInfo 테스트
class UserInfoTest(APITransactionTestCase):

    # test user 생성
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

    # userinfo 생성 (success : 201)
    def _create_userinfo(self):
        url = '/userinfo/'
        data = {'name' : 'hello'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserInfo.objects.count(), 1)
        self.assertEqual(UserInfo.objects.get().name, 'hello')

    # userinfo 얻기 및 push_id 변경 (success : 200)
    def _get_userinfo(self):
        url = '/userinfo/'
        push_id = "adawwfqhifhaifhwa"
        response = self.client.get(url, **{'HTTP_PUSHTOKEN':push_id})
        get_push_id = json.loads(response.content.decode('utf-8'))[0]["push_id"]
        self.assertEqual(get_push_id, push_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # userinfo 변경 및 push_id 변경 (success : 200)
    def _put_userinfo(self):
        url = '/userinfo/'
        push_id = "put_userinfo"
        put_data = {'name': 'test1', 'weekdays_start':10, 'weekend_start':10}
        response = self.client.put(url, put_data, **{'HTTP_PUSHTOKEN': push_id})
        get_name = json.loads(response.content.decode('utf-8'))["name"]
        get_weekdays_start = json.loads(response.content.decode('utf-8'))["weekdays_start"]
        get_weekend_start = json.loads(response.content.decode('utf-8'))["weekend_start"]
        get_push_id = json.loads(response.content.decode('utf-8'))["push_id"]

        self.assertEqual(get_push_id, push_id)
        self.assertEqual(get_name, put_data['name'])
        self.assertEqual(get_weekdays_start, put_data['weekdays_start'])
        self.assertEqual(get_weekend_start, put_data['weekend_start'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # push 알림 확인했을 시 처리 (success : 200)
    def _push_userinfo(self):
        url = '/userinfo/push/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # userinfo 제거
    def _delete_userinfo(self):
        url = '/userinfo/'
        self.assertEqual(UserInfo.objects.count(), 1)
        response = self.client.delete(url)
        self.assertEqual(UserInfo.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_main(self):
        print('------------------UserInfoTest Start------------------')
        self._create_userinfo()
        print('Success : UserInfoTest_create_userinfo')
        self._get_userinfo()
        print('Success : UserInfoTest_get_userinfo')
        self._put_userinfo()
        print('Success : UserInfoTest_put_userinfo')
        self._push_userinfo()
        print('Success : UserInfoTest_push_userinfo')
        self._delete_userinfo()
        print('Success : UserInfoTest_delete_userinfo')
        print('')

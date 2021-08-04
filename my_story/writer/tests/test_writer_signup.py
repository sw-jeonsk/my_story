import os
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


class TestWriterSignUp(TestCase):
    def setUp(self) -> None:
        self.signup_api = "/api/{}/writer/signup/".format(VERSION)
        return super().setUp()

    def test_signup_201_ok(self):
        """성공 처리"""
        response = self.client.post(
            self.signup_api,
            {"name": "jsk", "email": "qaz0169@naver.com", "password": "ain190409!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 201)

    def test_signup_email_error(self):
        """이메일 관련 에러"""
        # 이메일 규칙중 @이 없을 경우에 대한 에러 처리
        response = self.client.post(
            self.signup_api,
            {"name": "jsk", "email": "qaz0169naver.com", "password": "ain190409!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    def test_signup_name_error(self):
        """이름 관련 에러"""

        # 이름 길이가 1글자일때 에러
        response = self.client.post(
            self.signup_api,
            {"name": "j", "email": "qaz0169@naver.com", "password": "ain190409!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    def test_signup_password_error(self):
        """password 관련 에러"""

        # 패스워드 길이 에러
        response = self.client.post(
            self.signup_api,
            {"name": "jsk", "email": "qaz0169@naver.com", "password": "ain"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

        # 패스워드 영문자로만 진행시 에러
        response = self.client.post(
            self.signup_api,
            {"name": "jsk", "email": "qaz0169@naver.com", "password": "jaajsknaa"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

        # 패스워드 영문자 + 특수문자로만 진행시 에러
        response = self.client.post(
            self.signup_api,
            {"name": "jsk", "email": "qaz0169@naver.com", "password": "jaajsknaa!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

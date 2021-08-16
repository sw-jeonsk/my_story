import os
import pdb
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION
from utils.response_detail import ResponseDetail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestWriterLogin(TestCase):
    def setUp(self) -> None:
        # 회원가입
        self.signup_api = "/api/{}/writer".format(VERSION)
        self.login_api = "/api/{}/login".format(VERSION)
        self.email = "qaz0169@naver.com"
        self.password = "ain190409!"

        self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": self.email,
                "password": self.password,
            },
        )

        return super().setUp()

    def test_login_200_ok(self):
        """성공 처리"""
        response = self.client.post(
            self.login_api, {"email": self.email, "password": self.password}
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual("id" in response.json().keys(), True)
        self.assertEqual("access" in response.json().keys(), True)
        self.assertEqual("refresh" in response.json().keys(), True)

    def test_login_400_no_email(self):
        """이메일 파라미터 없음 에러 처리"""
        response = self.client.post(self.login_api, {"password": self.password})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.EMAIL_REQUIRED)

    def test_login_400_no_password(self):
        """비밀번호 파라미터 없음 에러 처리"""
        response = self.client.post(self.login_api, {"email": self.email})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_REQUIRED)

    def test_login_401_does_not_exist_email(self):
        """없는 이메일 계정 에러 처리"""
        email = "qaz0169_test@naver.com"
        response = self.client.post(self.login_api, {"email": email, "password": self.password})
        print(response.json())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], ResponseDetail.UNAUTHORIZED_VALIDATE)

    def test_login_401_wrong_password(self):
        """잘못된 패스워드"""
        password = "testtest123!!"
        response = self.client.post(self.login_api, {"email": self.email, "password": password})
        print(response.json())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], ResponseDetail.UNAUTHORIZED_VALIDATE)

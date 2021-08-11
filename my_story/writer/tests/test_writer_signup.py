from utils.response_detail import ResponseDetail
import os
import pdb
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestWriterSignUp(TestCase):
    def setUp(self) -> None:
        self.signup_api = "/api/{}/writer".format(VERSION)
        return super().setUp()

    def test_signup_201_ok(self):
        """성공 처리"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
                "password": "ain190409!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 201)

    def test_signup_no_email(self):
        """이메일 파라미터 없음"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "password": "ain190409!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.EMAIL_REQUIRED)

    def test_signup_email_error(self):
        """이메일 관련 에러"""
        # 이메일 규칙중 @이 없을 경우에 대한 에러 처리
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169naver.com",
                "password": "ain190409!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    def test_signup_name_error(self):
        """이름 관련 에러"""

        # 이름 길이가 1글자일때 에러
        response = self.client.post(
            self.signup_api,
            {
                "name": "j",
                "email": "qaz0169@naver.com",
                "password": "ain190409!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    # password 관련 에러
    def test_signup_password_error_01(self):
        """패스워드 길이 에러"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
                "password": "ain",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_VALIDATE)

    def test_signup_password_error_02(self):
        """패스워드 영문자로만 진행시 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
                "password": "jaajsknaa",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_VALIDATE)

    def test_signup_password_error_03(self):
        """패스워드 영문자 + 특수문자로만 진행시 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
                "password": "jaajsknaa!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_VALIDATE)

    def test_signup_password_error_04(self):
        """패스워드 숫자 + 특수문자로만 진행시 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
                "password": "12312412!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_VALIDATE)

    def test_signup_password_error_05(self):
        """패스워드 공백 포함으로 진행시 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
                "password": "123asdfasdf !",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_VALIDATE)

    def test_signup_no_email_error(self):
        """이메일 파라미터 없을때 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "password": "123asdfasdf!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.json()["detail"], ResponseDetail.EMAIL_REQUIRED)
        self.assertEqual(response.status_code, 400)

    def test_signup_empty_email_error(self):
        """이메일 파라미터 빈값 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "",
                "password": "123asdfasdf!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.EMAIL_BLANK)

    def test_signup_no_password_error(self):
        """패스워드 파라미터 없을때 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "jsk",
                "email": "qaz0169@naver.com",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_REQUIRED)
        self.assertEqual(response.status_code, 400)

    def test_signup_empty_password_error(self):
        """패스워드 파라미터 빈값 실패"""
        response = self.client.post(
            self.signup_api,
            {"name": "jsk", "email": "qaz0169@naver.com", "password": ""},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.PASSWORD_BLANK)

    def test_signup_no_name_error(self):
        """이름 파라미터 없을때 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "email": "qaz0169@naver.com",
                "password": "123asdfasdf!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.NAME_REQUIRED)

    def test_signup_empty_name_error(self):
        """이름 파라미터 없을때 실패"""
        response = self.client.post(
            self.signup_api,
            {
                "name": "",
                "email": "qaz0169@naver.com",
                "password": "123asdfasdf!",
            },
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], ResponseDetail.NAME_BLANK)

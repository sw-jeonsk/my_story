from utils.response_detail import ResponseDetail
import os
import pdb
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestWriterSignUp(TestCase):
    def setUp(self) -> None:
        # 회원가입
        self.signup_api = "/api/{}/writer".format(VERSION)

        return super().setUp()

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

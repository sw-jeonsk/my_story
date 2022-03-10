from utils.response_detail import ResponseDetail
import os
from django.test import TestCase
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestWriter(TestCase):
    def setUp(self) -> None:
        # 회원가입
        self.signup_api = "/api/{}/writer".format(VERSION)
        self.writer_api = "/api/{}/writer".format(VERSION)
        self.login_api = "/api/{}/login".format(VERSION)
        self.email = "qaz0169aa@naver.com"
        self.password = "ain190409!"

        self.client.post(
            self.writer_api,
            {
                "name": "jsk",
                "email": self.email,
                "password": self.password,
            },
        )
        # login 진행
        self.response = self.client.post(
            self.login_api, {"email": self.email, "password": self.password}
        )

    # password 관련 에러
    def test_get_404_no_writer(self):
        """없는 유저로 진행"""
        writer_id = "asdfasdfasdf"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.get(self.writer_api + "?id={}".format(writer_id), **header)
        print(response.json())
        self.assertEqual(response.status_code, 404)

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
        self.assertEqual(response.json()["detail"], ResponseDetail.BLANK)

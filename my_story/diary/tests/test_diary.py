from utils.response_detail import ResponseDetail
import os
import pdb
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestDiary(TestCase):
    def setUp(self) -> None:
        # 회원가입
        self.writer_api = "/api/{}/writer".format(VERSION)
        self.login_api = "/api/{}/login".format(VERSION)
        self.diary_api = "/api/{}/diary".format(VERSION)
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
    def test_diary_create_200_ok(self):
        """diary 추가 진행"""

        body = dict()
        body["writer"] = self.response.json()["id"]
        body["title"] = "title"
        body["contents"] = "contents"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.post(self.diary_api, body, **header)
        print(response.json())
        self.assertEqual(response.status_code, 200)

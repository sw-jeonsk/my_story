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

    # diary 추가 성공
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
        self.assertEqual(response.status_code, 201)

    # 권한 문제
    def test_diary_401_no_authorization(self):
        """diary 추가 진행"""

        body = dict()
        body["writer"] = self.response.json()["id"]
        body["title"] = "title"
        body["contents"] = "contents"

        response = self.client.post(self.diary_api, body)
        print(response.json())
        self.assertEqual(response.status_code, 401)

    # parameter 없을 경우
    def test_diary_400_no_writer(self):
        """diary 추가 진행"""

        body = dict()
        body["title"] = "title"
        body["contents"] = "contents"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.post(self.diary_api, body, **header)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    # parameter 없을 경우
    def test_diary_400_no_title(self):
        """diary 추가 진행"""

        body = dict()
        body["writer"] = self.response.json()["id"]
        body["contents"] = "contents"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.post(self.diary_api, body, **header)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    # parameter 없을 경우
    def test_diary_400_no_contents(self):
        """diary 추가 진행"""

        body = dict()
        body["writer"] = self.response.json()["id"]
        body["title"] = "title"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.post(self.diary_api, body, **header)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    # parameter 없을 경우
    def test_diary_list(self):
        """diary 추가 진행"""

        body = dict()
        body["writer"] = self.response.json()["id"]
        body["title"] = "title"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.post(self.diary_api, body, **header)
        print(response.json())
        self.assertEqual(response.status_code, 400)

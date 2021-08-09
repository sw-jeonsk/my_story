import os
import pdb
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestWriterGet(TestCase):
    def setUp(self) -> None:
        # 회원가입
        self.writer_api = "/api/{}/writer".format(VERSION)
        self.login_api = "/api/{}/login".format(VERSION)
        self.email = "qaz0169@naver.com"
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

        return super().setUp()

    # def test_get_200_ok(self):
    #     """성공 처리"""
    #     response = self.client.post(
    #         self.writer_api + "/{}"., {"email": self.email, "password": self.password}
    #     )
    #     self.assertEqual(response.status_code, 200)

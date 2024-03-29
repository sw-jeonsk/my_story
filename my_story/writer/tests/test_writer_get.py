from utils.response_detail import ResponseDetail
import os
from django.test import TestCase
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class TestWriterGet(TestCase):
    def setUp(self) -> None:
        # 회원가입
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

        return super().setUp()

    def test_get_200_ok(self):
        """성공 처리"""
        writer_id = self.response.json()["id"]
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.get(self.writer_api + "?id={}".format(writer_id), **header)
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_404_no_writer(self):
        """없는 유저로 진행"""
        writer_id = "asdfasdfasdf"
        access = self.response.json()["access"]

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.get(self.writer_api + "?id={}".format(writer_id), **header)
        print(response.json())
        self.assertEqual(response.status_code, 404)

    def test_get_401_no_authorization(self):
        """token 인증 없을 경우 에러 처리"""
        writer_id = self.response.json()["id"]

        response = self.client.get(self.writer_api + "?id={}".format(writer_id))
        print(response.json())
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], ResponseDetail.UNAUTHORIZED_VALIDATE)

    def test_get_401_wrong_authorization(self):
        """잘못된 토큰 처리"""
        writer_id = self.response.json()["id"]
        access = "asdfasdfasdfasdf"

        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(access)}

        response = self.client.get(self.writer_api + "?id={}".format(writer_id), **header)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["detail"], ResponseDetail.UNAUTHORIZED_VALIDATE)

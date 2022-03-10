import os
from django.test import TestCase
from app.settings import VERSION
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()


class TestWriterSingle(TestCase):
    def setUp(self) -> None:
        self.signup_api = "/api/{}/writer".format(VERSION)
        self.email_duplicate_api = "/api/{}/writer/email-check".format(VERSION)
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

    def test_email_200_ok(self):
        """메일 중복 확인 테스트"""

        response = self.client.post(self.email_duplicate_api, {"email": "test@a-in.co"})
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_email_400_duplicate(self):
        """메일 중복 확인 테스트"""

        response = self.client.post(self.email_duplicate_api, {"email": self.email})
        print(response.json())
        self.assertEqual(response.status_code, 400)

    def test_email_400_no_email(self):
        """메일 파라미터 없음"""

        response = self.client.post(self.email_duplicate_api)
        print(response.json())
        self.assertEqual(response.status_code, 400)

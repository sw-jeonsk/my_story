import os
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


class TestWriter(TestCase):
    def test_writer_create_201_ok(self):
        """성공 처리"""
        response = self.client.post(
            "/api/{}/writer/signup/".format(VERSION),
            {"name": "jsk", "email": "qaz0169@naver.com", "password": "ain190409!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 201)

    def test_writer_email_error01(self):
        """이메일 규칙중 @이 없을 경우에 대한 에러 처리"""
        response = self.client.post(
            "/api/{}/writer/signup/".format(VERSION),
            {"name": "jsk", "email": "qaz0169naver.com", "password": "ain190409!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

    def test_writer_name_error(self):
        """이름 길이가 1글자일때 에러"""
        response = self.client.post(
            "/api/{}/writer/signup/".format(VERSION),
            {"name": "j", "email": "qaz0169naver.com", "password": "ain190409!"},
        )
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 400)

import os
from django.test import TestCase
from writer.models import Writer
from app.settings import VERSION

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


class TestWriterSingle(TestCase):
    def setUp(self) -> None:
        self.email_duplicate_api = "/api/{}/writer/email-check".format(VERSION)
        return super().setUp()

    def test_email_duplicate(self):
        """메일 중복 확인 테스트"""
        # TODO
        pass

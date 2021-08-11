from rest_framework.exceptions import APIException
from .response_detail import ResponseDetail


class Exception(APIException):
    detail_code = 200

    @classmethod
    def as_md(self):
        return '\n\n> **%s**\n```\n{\n\t"status_code": "%s"\n\t"detail_code": "%s"\n\t"detail": "%s"\n\t"request":{[request 데이터]}\n}\n```' % (
            self.status_code,
            self.status_code,
            self.detail_code,
            self.default_detail,
        )


class EmailRequiredException(Exception):
    status_code = 400
    detail_code = "required"
    default_detail = ResponseDetail.EMAIL_REQUIRED


class NameRequiredException(Exception):
    status_code = 400
    detail_code = "required"
    default_detail = ResponseDetail.NAME_REQUIRED


class PasswordRequiredException(Exception):
    status_code = 400
    detail_code = "required"
    default_detail = ResponseDetail.PASSWORD_REQUIRED


class EmailValidateException(Exception):
    status_code = 400
    detail_code = "error"
    default_detail = ResponseDetail.EMAIL_VALIDATE


class NameValidateException(Exception):
    status_code = 400
    detail_code = "error"
    default_detail = ResponseDetail.NAME_VALIDATE


class PasswordValidateException(Exception):
    status_code = 400
    detail_code = "error"
    default_detail = ResponseDetail.PASSWORD_VALIDATE


class EmailDuplicateException(Exception):
    status_code = 400
    detail_code = "duplicate"
    default_detail = ResponseDetail.EMAIL_DUPLICATE
